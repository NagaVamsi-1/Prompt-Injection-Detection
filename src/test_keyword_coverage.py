import json
from attack_keywords import attack_keywords

# CHANGE THIS FILE NAME WHEN TESTING
DATASET_FILE = r"C:\Users\nagav\PromptInjectionDetector\data\processed\clean\combined_dataset_final.json"

with open(DATASET_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

matched = 0

for item in data:
    text = item["text"].lower()

    if any(keyword in text for keyword in attack_keywords):
        matched += 1

total = len(data)

print("=" * 40)
print("Dataset:", DATASET_FILE)
print("Total Samples:", total)
print("Matched Samples:", matched)
print("Coverage: {:.2f}%".format((matched / total) * 100))
print("=" * 40)