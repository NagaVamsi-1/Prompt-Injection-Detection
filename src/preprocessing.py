# import json
# import re
# from pathlib import Path

# # -----------------------------
# # File Paths
# # -----------------------------
# DATA_DIR = Path("data/processed")

# FILES = [
#     "standardized_benign_2000.json",
#     "standardized_instruction_override_2000.json",
#     "standardized_jailbreak_1542.json"
# ]

# # -----------------------------
# # Text Cleaning Function
# # -----------------------------
# def clean_text(text):
#     if not isinstance(text, str):
#         return ""

#     # lowercase
#     text = text.lower()

#     # remove extra spaces/newlines/tabs
#     text = re.sub(r"\s+", " ", text)

#     # remove leading/trailing spaces
#     text = text.strip()

#     return text

# # -----------------------------
# # Process Each Dataset
# # -----------------------------
# for file_name in FILES:

#     input_path = DATA_DIR / file_name

#     with open(input_path, "r", encoding="utf-8") as f:
#         data = json.load(f)

#     cleaned_data = []

#     for item in data:

#         item["text"] = clean_text(item["text"])

#         cleaned_data.append(item)

#     output_name = file_name.replace(".json", "_clean.json")
#     output_path = DATA_DIR / output_name

#     with open(output_path, "w", encoding="utf-8") as f:
#         json.dump(cleaned_data, f, indent=4, ensure_ascii=False)

#     print(f"✓ Saved: {output_name}")

# print("\nAll datasets cleaned successfully!")
import json
from collections import Counter

FILES = [
    "data/standardized_benign_2000.json",
    "data/standardized_instruction_override_2000.json",
    "data/standardized_jailbreak_1542.json"
]

all_texts = []

for file in FILES:
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)

    texts = [item["text"].strip().lower() for item in data]

    total = len(texts)
    unique = len(set(texts))
    duplicates = total - unique

    print(f"\n{file}")
    print(f"Total samples      : {total}")
    print(f"Unique samples     : {unique}")
    print(f"Duplicate samples  : {duplicates}")

    all_texts.extend(texts)

# Cross-dataset duplicates
print("\n" + "="*50)

total_all = len(all_texts)
unique_all = len(set(all_texts))
duplicates_all = total_all - unique_all

print("ALL DATASETS COMBINED")
print(f"Total samples      : {total_all}")
print(f"Unique samples     : {unique_all}")
print(f"Duplicate samples  : {duplicates_all}")

# Show duplicate texts
counter = Counter(all_texts)

dupes = [(text, count) for text, count in counter.items() if count > 1]

print(f"\nNumber of unique duplicated prompts: {len(dupes)}")

for text, count in sorted(dupes, key=lambda x: x[1], reverse=True)[:20]:
    print("\n" + "-"*80)
    print(f"Occurrences: {count}")
    print(text[:300])