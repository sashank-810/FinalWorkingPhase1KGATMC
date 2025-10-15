import json5
import json

def fix_json5(file_path, output_path=None):
    with open(file_path, 'r') as f:
        data = json5.load(f)  # Parses JSON5 syntax safely

    output_path = output_path or file_path
    with open(output_path, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"✅ Converted from JSON5 → Valid JSON at {output_path}")

# Example usage
fix_json5("FinalWorkingPhase1KGATMC/bulk_dataset.json", "output.json")
