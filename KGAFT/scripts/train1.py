import yaml
import torch
from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments, BitsAndBytesConfig, EarlyStoppingCallback
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from trl import SFTTrainer

def format_prompt(example):
    """
    Formats a single structured MCQ data example for training.
    The model learns to output the correct letter.
    """
    question = example['question']
    answer = example['answer']

    # Format the options from the dictionary into a clear, readable list

    # The final prompt format for training
    return (
        f"Question: {question}\n\n"
        f"Answer: {answer}"
    )

def main():
    # 1. Load configuration from YAML file
    with open('/home/resiliente2003/vishnu/KGAFT/config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    print("Configuration loaded successfully.")

    # 2. Load and prepare the datasets
    train_dataset = load_dataset("json", data_files=config['train_dataset_path'], split="train")
    eval_dataset = load_dataset("json", data_files=config['validation_dataset_path'], split="train")
    
    print(f"Training dataset size: {len(train_dataset)}")
    print(f"Validation dataset size: {len(eval_dataset)}")
    
    # 3. Load tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained(config['model_name_or_path'], trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
        
    quantization_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.bfloat16
    )
    tokenizer.max_seq_length = 1024
    
    model_kwargs = {
        "quantization_config": quantization_config,
        "torch_dtype": torch.bfloat16,
        "device_map": "auto",
        "trust_remote_code": True
    }
    if config.get('use_flash_attention_2', False):
        model_kwargs["use_flash_attention_2"] = True

    model = AutoModelForCausalLM.from_pretrained(
        config['model_name_or_path'],
        **model_kwargs
    )
    model.config.use_cache = False
    
    # 4. Configure PEFT (LoRA)
    peft_config = LoraConfig(
        r=config['lora_r'],
        lora_alpha=config['lora_alpha'],
        lora_dropout=config['lora_dropout'],
        target_modules=config['lora_target_modules'],
        bias="none",
        task_type="CAUSAL_LM",
    )
    
    model = prepare_model_for_kbit_training(model)
    model = get_peft_model(model, peft_config)

    # 5. Configure Training Arguments
    training_args = TrainingArguments(
        output_dir=config['output_dir'],
        num_train_epochs=config['num_train_epochs'],
        per_device_train_batch_size=config['per_device_train_batch_size'],
        gradient_accumulation_steps=config['gradient_accumulation_steps'],
        optim=config['optim'],
        learning_rate= 1e-5,
        fp16=config['fp16'],
        logging_steps=config['logging_steps'],
        save_strategy="epoch",
        # --- CORRECTED ARGUMENT NAME ---
        eval_strategy="epoch", # Changed from 'eval_strategy'
        # --- END OF CORRECTION ---
        load_best_model_at_end=True,
        metric_for_best_model="eval_loss",
        greater_is_better=False,
    )

    # 6. Initialize the SFTTrainer
    trainer = SFTTrainer(
        model=model,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset,
        peft_config=peft_config,
        formatting_func=format_prompt,
        args=training_args,
        callbacks=[EarlyStoppingCallback(early_stopping_patience=3)],
    )

    # 7. Start training
    print("Starting fine-tuning...")
    trainer.train()
    print("Fine-tuning completed.")

    # 8. Save the fine-tuned adapter model
    final_model_path = f"{config['output_dir']}/final_model"
    trainer.save_model(final_model_path)
    print(f"Model saved to {final_model_path}")

if __name__ == "__main__":
    main()