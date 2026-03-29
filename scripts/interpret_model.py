import pickle, os
import pandas as pd
import numpy as np

MODEL_PATH = os.path.expanduser("~/CD_Lab_Project/data/processed/model.pkl")

def explain_intelligence():
    with open(MODEL_PATH, 'rb') as f:
        pipeline = pickle.load(f)
    
    # Extract the vectorizer and the classifier from the pipeline
    vec = pipeline.named_steps['tfidf']
    clf = pipeline.named_steps['etc']
    
    feature_names = vec.get_feature_names_out()
    importances = clf.feature_importances_
    
    # Sort and get top 20 features
    indices = np.argsort(importances)[-20:][::-1]
    
    print("\n--- Week 7: Model Intelligence Analysis ---")
    print(f"{'Keyword/Token':<25} | {'Influence Score'}")
    print("-" * 45)
    for i in indices:
        print(f"{feature_names[i]:<25} | {importances[i]:.4f}")

if __name__ == "__main__":
    explain_intelligence()
