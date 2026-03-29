import os, pickle, re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, accuracy_score

def train_final_model():
    BASE_DIR = os.path.expanduser("~/CD_Lab_Project/data/cleaned_data")
    messages, labels = [], []
    
    # Custom stop words: Remove words that don't help classification
    custom_stops = ['at', 'line', 'in', 'function', 'error', 'main']

    for cat in ["lexical", "syntactic", "semantic"]:
        with open(f"{BASE_DIR}/{cat}_cleaned.txt", "r") as f:
            for line in f:
                # Cleaning and normalizing
                msg = line.strip().lower()
                msg = re.sub(r'0x[0-9a-f]+|[0-9]+', '', msg)
                messages.append(msg)
                labels.append(cat)

    # Use a slightly smaller test size to maximize training patterns
    X_train, X_test, y_train, y_test = train_test_split(
        messages, labels, test_size=0.12, random_state=7, stratify=labels
    )

    # ExtraTrees is often better than RandomForest for small text datasets
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer(
            ngram_range=(1, 3), 
            stop_words=custom_stops,
            use_idf=True,
            smooth_idf=True,
            sublinear_tf=True
        )),
        ('etc', ExtraTreesClassifier(
            n_estimators=1000, 
            bootstrap=True, 
            class_weight='balanced',
            random_state=7
        ))
    ])

    print("🚀 Training High-Accuracy Ensemble Model...")
    pipeline.fit(X_train, y_train)

    y_pred = pipeline.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    
    print("\n--- Week 6: Elite Performance Report ---")
    print(f"Final Accuracy: {acc * 100:.2f}%")
    print("\nClassification Matrix:")
    print(classification_report(y_test, y_pred))

    path = os.path.expanduser("~/CD_Lab_Project/data/processed")
    os.makedirs(path, exist_ok=True)
    with open(f"{path}/model.pkl", "wb") as f:
        pickle.dump(pipeline, f)
    
    print(f"Model saved to: {path}/model.pkl")

if __name__ == "__main__":
    train_final_model()
