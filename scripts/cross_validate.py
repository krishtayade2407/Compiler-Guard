import os, pickle, random
import numpy as np
from sklearn.model_selection import cross_val_score, StratifiedKFold
from feature_engineering import prepare_features

def validate():
    print("Loading and Shuffling data for Elite Validation...")
    MODEL_PATH = os.path.expanduser("~/CD_Lab_Project/data/processed/model.pkl")
    with open(MODEL_PATH, 'rb') as f:
        pipeline = pickle.load(f)

    BASE_DIR = os.path.expanduser("~/CD_Lab_Project/data/cleaned_data")
    all_data = []
    for cat in ["lexical", "syntactic", "semantic"]:
        with open(f"{BASE_DIR}/{cat}_cleaned.txt", "r") as f:
            lines = f.readlines()
            # Sample 5000 from each category to get a balanced, manageable 15k set
            sampled = random.sample(lines, min(len(lines), 5000))
            for line in sampled:
                all_data.append((line.strip(), cat))

    # Shuffle everything
    random.shuffle(all_data)
    messages = [d[0] for d in all_data]
    labels = [d[1] for d in all_data]

    print(f"Running Stratified 5-Fold CV on {len(messages)} shuffled samples...")
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    scores = cross_val_score(pipeline, messages, labels, cv=skf)
    
    print("\n--- Week 7: Elite Reliability Report ---")
    print(f"Individual Fold Accuracies: {scores}")
    print(f"Mean Stability Accuracy: {scores.mean()*100:.2f}%")
    print(f"Standard Deviation (Risk): {scores.std():.4f}")

if __name__ == "__main__":
    validate()
