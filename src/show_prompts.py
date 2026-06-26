import json

DATASET_FILE = r"C:\Users\nagav\PromptInjectionDetector\data\processed\clean\standardized_instruction_override_2000_clean.json"

with open(DATASET_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

print("=" * 100)
print("TOTAL SAMPLES:", len(data))
print("=" * 100)

for i in range(10):
    print(f"\nPROMPT {i+1}")
    print("-" * 100)
    print(data[i]["text"])
    print("-" * 100)