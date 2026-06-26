import json
from attack_keywords import attack_keywords
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

DATASET_FILE = r"C:\Users\nagav\PromptInjectionDetector\data\processed\clean\combined_dataset_final.json"
with open(DATASET_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

y_true = []
y_pred = []

for item in data:

    text = item["text"].lower()

    true_label = item["label"]

    prediction = 0

    if any(keyword in text for keyword in attack_keywords):
        prediction = 1

    y_true.append(true_label)
    y_pred.append(prediction)

accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)

print("\nRULE-BASED DETECTOR RESULTS")
print("=" * 40)

print(f"Accuracy : {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall   : {recall:.4f}")
print(f"F1 Score : {f1:.4f}")