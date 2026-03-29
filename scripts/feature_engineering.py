import pandas as pd
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder

BASE_DIR = os.path.expanduser("~/CD_Lab_Project/data/cleaned_data")
CATEGORIES = ["lexical", "syntactic", "semantic"]

def prepare_features():
    messages = []
    labels = []
    for cat in CATEGORIES:
        file_path = os.path.join(BASE_DIR, f"{cat}_cleaned.txt")
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                for line in f:
                    if line.strip():
                        messages.append(line.strip())
                        labels.append(cat)
    tfidf = TfidfVectorizer(ngram_range=(1, 2))
    X = tfidf.fit_transform(messages)
    le = LabelEncoder()
    y = le.fit_transform(labels)
    return X, y, tfidf, le

def prepare_data():
    return prepare_features()

if __name__ == "__main__":
    prepare_features()
