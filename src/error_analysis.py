import json

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Dataset Path
DATASET_FILE = r"C:\Users\nagav\PromptInjectionDetector\data\processed\clean\combined_dataset_final.json"

# Load Dataset
with open(DATASET_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

texts = []
labels = []

for item in data:
    texts.append(item["text"])
    labels.append(item["label"])

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    texts,
    labels,
    test_size=0.2,
    random_state=42,
    stratify=labels
)

# TF-IDF Vectorization
vectorizer = TfidfVectorizer(
    max_features=10000,
    ngram_range=(1, 2)
)

X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Logistic Regression Model
model = LogisticRegression(
    max_iter=1000,
    class_weight="balanced"
)

model.fit(X_train_tfidf, y_train)

# Predictions
y_pred = model.predict(X_test_tfidf)

# Collect Errors
false_positives = []
false_negatives = []

for text, actual, pred in zip(X_test, y_test, y_pred):

    # False Positive
    if actual == 0 and pred == 1:
        false_positives.append(text)

    # False Negative
    elif actual == 1 and pred == 0:
        false_negatives.append(text)

# Display Results
print("\n")
print("=" * 80)
print("FALSE POSITIVES (Benign predicted as Attack)")
print("=" * 80)

for i, prompt in enumerate(false_positives[:10], start=1):
    print(f"\nFP {i}")
    print("-" * 80)
    print(prompt)

print("\n")
print("=" * 80)
print("FALSE NEGATIVES (Attack predicted as Benign)")
print("=" * 80)

for i, prompt in enumerate(false_negatives[:10], start=1):
    print(f"\nFN {i}")
    print("-" * 80)
    print(prompt)

print("\n")
print("=" * 80)
print("SUMMARY")
print("=" * 80)
print(f"Total False Positives : {len(false_positives)}")
print(f"Total False Negatives : {len(false_negatives)}")