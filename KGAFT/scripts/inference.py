import torch
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

def main():
    # Path to the base model and the fine-tuned adapter
    base_model_name = "microsoft/phi-2" # Must be the same as used in training
    adapter_path = "/home/resiliente2003/vishnu/KGAFT/results_phi2_finetuned/final_model" # Path where the adapter was saved

    # Configure quantization
    quantization_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.bfloat16
    )

    # Load the base model
    print("Loading base model...")
    base_model = AutoModelForCausalLM.from_pretrained(
        base_model_name,
        quantization_config=quantization_config,
        torch_dtype=torch.bfloat16,
        device_map="auto",
        trust_remote_code=True
    )
    
    tokenizer = AutoTokenizer.from_pretrained(base_model_name, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    # Load the PEFT model (adapter) on top of the base model
    print("Loading adapter...")
    model = PeftModel.from_pretrained(base_model, adapter_path)

    # --- Interactive Inference Loop ---
    print("\nModel ready for inference. Type 'exit' to quit.")
    while True:
        user_input = input("Enter your question: ")
        if user_input.lower() == 'exit':
            break

        # Format the prompt just like in training
        prompt = f"### Question:\n{user_input}\n\n### Answer:\n"
        
        # Tokenize the input
        inputs = tokenizer(prompt, return_tensors="pt", return_attention_mask=False).to("cuda")

        # Generate a response
        outputs = model.generate(**inputs, max_length=512, eos_token_id=tokenizer.eos_token_id)
        
        # Decode and print the response
        response_text = tokenizer.batch_decode(outputs)[0]
        
        # Clean up the output to show only the generated part
        # The generated text includes the prompt, so we remove it.
        generated_part = response_text[len(prompt):]
        print("---")
        print(f"Model Response:\n{generated_part.strip()}")
        print("---\n")

if __name__ == "__main__":
    main()