import json
import random

# --- Configuration ---
original_dataset_path = '/home/administrator/Desktop/AIDS/KGAFT/data/dummy_dataset.jsonl'
train_path = '/home/administrator/Desktop/AIDS/KGAFT/data/train.jsonl'
validation_path = '/home/administrator/Desktop/AIDS/KGAFT/data/validation.jsonl'
test_path = '/home/administrator/Desktop/AIDS/KGAFT/data/test.jsonl'

# Define the split ratios
train_ratio = 0.8  # 80% for training
validation_ratio = 0.1 # 10% for validation
# The rest (10%) will be for testing

# --- Main Script ---
print(f"Loading original dataset from {original_dataset_path}...")
with open(original_dataset_path, 'r', encoding='utf-8') as f:
    data = [json.loads(line) for line in f]

# Shuffle the dataset to ensure random distribution
random.shuffle(data)
print(f"Total examples: {len(data)}")

# Calculate split indices
train_end = int(train_ratio * len(data))
validation_end = int((train_ratio + validation_ratio) * len(data))

# Create the splits
train_data = data[:train_end]
validation_data = data[train_end:validation_end]
test_data = data[validation_end:]

print(f"Training set size: {len(train_data)}")
print(f"Validation set size: {len(validation_data)}")
print(f"Test set size: {len(test_data)}")

# Function to save a list of dictionaries to a .jsonl file
def save_to_jsonl(data_list, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        for entry in data_list:
            json.dump(entry, f)
            f.write('\n')

# Save the new datasets
save_to_jsonl(train_data, train_path)
save_to_jsonl(validation_data, validation_path)
save_to_jsonl(test_data, test_path)

print("\nSuccessfully created train.jsonl, validation.jsonl, and test.jsonl in the 'data' directory.")