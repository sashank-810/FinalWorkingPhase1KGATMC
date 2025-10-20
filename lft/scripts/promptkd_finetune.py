"""
Full Fine-Tuning Script (LfT Final Stage, Config Integrated)
------------------------------------------------------------
Uses STUDENT_MODEL and COMBINED dataset path from configs/nim_config.yaml.
Performs full fine-tuning across all parameters.

✅ Compatible with multi-GPU Accelerate.
✅ Automatically handles missing pad_token.
✅ Safe device-map handling (avoids distributed conflicts).
"""

import os
import json
import argparse
from datasets import Dataset
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    Trainer,
    TrainingArguments,
    DataCollatorForLanguageModeling,
)
from scripts.utils import load_cfg


def main():
    # -----------------------------
    # Parse CLI config argument
    # -----------------------------
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="configs/hf_config.yaml", help="Path to config file")
    args = parser.parse_args()

    # -----------------------------
    # Load configuration
    # -----------------------------
    cfg = load_cfg(args.config)
    # Overwrite with domain-specific student setup if exists
    if os.path.exists("configs/nim_config.yaml"):
        cfg = load_cfg("configs/nim_config.yaml")

    model_name = cfg["STUDENT_MODEL"]
    data_path = cfg["DATA_PATHS"]["COMBINED"]
    output_dir = cfg["MODEL_OUTPUT"]

    # -----------------------------
    # Load dataset
    # -----------------------------
    print(f"🧠 Loading dataset → {data_path}")
    with open(data_path, "r") as f:
        data = json.load(f)

    dataset = Dataset.from_list([
        {"text": f"Question: {ex['question']}\nAnswer: {ex['answer']}"} for ex in data
    ])
    print(f"📚 Total training examples: {len(dataset)}")

    # -----------------------------
    # Load tokenizer & model
    # -----------------------------
    print(f"🚀 Loading model → {model_name}")
    tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=False)

    # Ensure padding token exists
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
        print(f"Set tokenizer.pad_token = {tokenizer.pad_token}")

    # Detect distributed mode (accelerate sets WORLD_SIZE/LOCAL_RANK)
    is_distributed = int(os.environ.get("WORLD_SIZE", "1")) > 1 or int(os.environ.get("LOCAL_RANK", "-1")) >= 0

    if is_distributed:
        # Accelerate will manage GPU placement — no device_map here!
        model = AutoModelForCausalLM.from_pretrained(
            model_name,
            device_map=None,
            low_cpu_mem_usage=True,
            dtype="auto",
        )
        print("✅ Model loaded for distributed training (device_map=None, low_cpu_mem_usage=True).")
    else:
        # Single-process: device_map='auto' is fine
        model = AutoModelForCausalLM.from_pretrained(
            model_name,
            device_map="auto",
            dtype="auto",
        )
        print("✅ Model loaded with device_map='auto' (single process).")

    # -----------------------------
    # Tokenization function
    # -----------------------------
    def tokenize_fn(example):
        return tokenizer(
            example["text"],
            truncation=True,
            padding="max_length",
            max_length=1024,
        )

    tokenized = dataset.map(tokenize_fn, batched=True)

    # -----------------------------
    # Data collator
    # -----------------------------
    collator = DataCollatorForLanguageModeling(
        tokenizer=tokenizer,
        mlm=False,  # causal LM, not masked LM
    )

    # -----------------------------
    # Training configuration
    # -----------------------------
    training_args = TrainingArguments(
        output_dir=output_dir,
        per_device_train_batch_size=2,
        gradient_accumulation_steps=8,
        learning_rate=5e-5,
        num_train_epochs=2,
        fp16=True,
        save_strategy="epoch",
        save_total_limit=2,
        logging_steps=50,
        report_to="none",
        warmup_steps=100,
        weight_decay=0.01,
    )

    # -----------------------------
    # Trainer setup
    # -----------------------------
    trainer = Trainer(
        model=model,
        args=training_args,
        data_collator=collator,
        train_dataset=tokenized,
    )

    # -----------------------------
    # Fine-tuning
    # -----------------------------
    print("🧩 Starting FULL fine-tuning (research-grade)...")
    trainer.train()

    # -----------------------------
    # Save results
    # -----------------------------
    model.save_pretrained(output_dir)
    tokenizer.save_pretrained(output_dir)
    print(f"✅ Full fine-tuned model saved → {output_dir}")


if __name__ == "__main__":
    main()
