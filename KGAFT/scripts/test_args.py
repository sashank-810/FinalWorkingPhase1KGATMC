from transformers import TrainingArguments

print("Attempting to create TrainingArguments...")

try:
    args = TrainingArguments(
        output_dir="./test_results",
        evaluation_strategy="epoch",  # This is the argument causing the error
    )
    print("\nSUCCESS: TrainingArguments object created successfully.")
    print(f"Evaluation strategy is set to: {args.evaluation_strategy}")

except TypeError as e:
    print(f"\nFAILURE: The script failed as expected.")
    print(f"Error: {e}")