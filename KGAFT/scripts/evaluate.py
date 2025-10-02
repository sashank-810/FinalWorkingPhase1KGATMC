import torch
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer
from datasets import load_dataset
from tqdm import tqdm
import os
from difflib import SequenceMatcher # We'll use this for robust string comparison

# In scripts/evaluate.py

# --- Configuration ---
base_model_name = "Qwen/Qwen3-4B-Thinking-2507"  # The base model architecture
adapter_path = "/home/resiliente2003/vishnu/KGAFT/results_qwen4b_finetuned3/final_model"
test_dataset_path = "/home/resiliente2003/vishnu/KGAFT/data/test.jsonl" 

# --- Load Models and Tokenizer ---
print("Loading models...")

# --- Step 1: Load the Fine-Tuned Model ---
# First, load a copy of the base model to apply the adapter to.
finetuned_base = AutoModelForCausalLM.from_pretrained(
    base_model_name,
    torch_dtype=torch.bfloat16,
    device_map="auto",
    trust_remote_code=True
)
# Now, apply the adapter to this copy to create the full fine-tuned model.
finetuned_model = PeftModel.from_pretrained(finetuned_base, adapter_path)
print("Fine-tuned model loaded.")

# --- Step 2: Load a SEPARATE, CLEAN Base Model ---
# This loads a completely fresh, unmodified copy of the base model for a fair comparison.
base_model = AutoModelForCausalLM.from_pretrained(
    base_model_name,
    torch_dtype=torch.bfloat16,
    device_map="auto",
    trust_remote_code=True
)
print("Separate base model loaded.")

# --- Step 3: Load the Tokenizer (only needs to be done once) ---
tokenizer = AutoTokenizer.from_pretrained(base_model_name, trust_remote_code=True)
tokenizer.pad_token = tokenizer.eos_token

# --- Step 4: Load the Dataset ---
dataset = load_dataset("json", data_files=test_dataset_path, split="train")

# --- Evaluation Loop ---
base_correct = 0
finetuned_correct = 0
total = len(dataset)

print("\nStarting robust MCQ evaluation...")
for example in tqdm(dataset, desc="Evaluating"):
    question = example['question']
    options = example['options'] # The dict {'A': '...', 'B': '...'}
    ground_truth_letter = example['answer'].strip().upper()

    options_str = "\n".join([f"{key}) {value}" for key, value in options.items()])
    
    prompt = (
        f"Question: {question}\n\n"
        f"Options:\n{options_str}\n\n"
        f"Answer:"
    )
    
    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")

    # Generate responses
    base_outputs = base_model.generate(**inputs, max_new_tokens=50, eos_token_id=tokenizer.eos_token_id)
    base_generated_text = tokenizer.batch_decode(base_outputs, skip_special_tokens=True)[0]
    
    finetuned_outputs = finetuned_model.generate(**inputs, max_new_tokens=50, eos_token_id=tokenizer.eos_token_id)
    finetuned_generated_text = tokenizer.batch_decode(finetuned_outputs, skip_special_tokens=True)[0]

    base_model_output = base_generated_text.split("Answer:")[-1].strip()
    finetuned_model_output = finetuned_generated_text.split("Answer:")[-1].strip()
    
    # --- THIS IS THE NEW, ROBUST LOGIC ---
    def get_best_match(model_gen_text, options_dict):
        best_match_letter = None
        highest_similarity = -1.0
        
        # Compare the model's output against each option's text
        for letter, option_text in options_dict.items():
            similarity = SequenceMatcher(None, model_gen_text.lower(), option_text.lower()).ratio()
            if similarity > highest_similarity:
                highest_similarity = similarity
                best_match_letter = letter
        return best_match_letter

    # Find the best matching option for each model's output
    base_choice = get_best_match(base_model_output, options)
    finetuned_choice = get_best_match(finetuned_model_output, options)

    # Check if the chosen option is the correct one
    if base_choice == ground_truth_letter:
        base_correct += 1
        
    if finetuned_choice == ground_truth_letter:
        finetuned_correct += 1
    # --- END OF NEW LOGIC ---

# --- Calculate and Report Final Scores ---
base_accuracy = (base_correct / total) * 100
finetuned_accuracy = (finetuned_correct / total) * 100

print("\n--- ✅ Evaluation Finished ---")
print(f"Total Questions: {total}")
print("-" * 30)
print("📊 Base Model Performance:")
print(f"   Correct Answers: {base_correct}")
print(f"   Accuracy: {base_accuracy:.2f}%")
print("-" * 30)
print("🚀 Fine-Tuned Model Performance:")
print(f"   Correct Answers: {finetuned_correct}")
print(f"   Accuracy: {finetuned_accuracy:.2f}%")
print("-" * 30)