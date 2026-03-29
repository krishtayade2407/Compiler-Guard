import os, pickle, time, numpy as np
def run_grand_demo():
    MODEL_PATH = os.path.expanduser("~/CD_Lab_Project/data/processed/model.pkl")
    DATA_DIR = os.path.expanduser("~/CD_Lab_Project/data/cleaned_data")
    print("\n" + "="*70 + "\n PHASE 1: BIG DATA REPOSITORY VERIFICATION \n" + "="*70)
    total = 0
    for cat in ["lexical", "syntactic", "semantic"]:
        path = f"{DATA_DIR}/{cat}_cleaned.txt"
        count = sum(1 for line in open(path)) if os.path.exists(path) else 0
        print(f" > {cat.upper():<10} Data: {count:,} samples verified.")
        total += count
    print(f"\nTOTAL DATA VOLUME: {total:,} Samples\n")
    time.sleep(1)
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)
    print("="*70 + "\n PHASE 2: LIVE INTERACTIVE INFERENCE \n" + "="*70)
    while True:
        user_input = input("\nEnter Error Log -> ").strip()
        if user_input.lower() in ['exit', 'quit']: break
        if not user_input: continue
        pred = model.predict([user_input])[0]
        conf = np.max(model.predict_proba([user_input])[0]) * 100
        print(f"ANALYSIS  : [ {pred.upper()} ]\nCONFIDENCE: {conf:.2f}%")
run_grand_demo()
