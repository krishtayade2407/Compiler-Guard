import pickle, os

MODEL_PATH = os.path.expanduser("~/CD_Lab_Project/data/processed/model.pkl")

# Manual Expert Rules (The Anchor Keywords)
EXPERT_RULES = {
    "lexical": ["stray", "invalid suffix", "multi-character", "unknown escape"],
    "semantic": ["undeclared", "incompatible", "argument", "storage size", "invalid operands"],
    "syntactic": ["expected", "before", "suggest", "missing", "unbalanced"]
}

def hybrid_predict(log_message):
    log_lower = log_message.lower()
    
    # 1. Check Expert Rules First
    for category, keywords in EXPERT_RULES.items():
        for word in keywords:
            if word in log_lower:
                return f"{category.upper()} (Expert Rule)"
    
    # 2. If no rule matches, use the ML Model
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)
    prediction = model.predict([log_message])[0]
    return f"{prediction.upper()} (ML Model)"

def main():
    print("\n--- Week 6: Hybrid ML-Expert Classifier ---")
    while True:
        log = input("\nEnter Error Log (or 'exit'): ")
        if log.lower() == 'exit': break
        result = hybrid_predict(log)
        print(f"Result: {result}")

if __name__ == "__main__":
    main()
