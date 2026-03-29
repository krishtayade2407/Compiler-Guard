import os

BASE_DIR = os.path.expanduser("~/CD_Lab_Project/data/cleaned_data")

def generate_report():
    print("--- Compiler Error Data Distribution Report ---")
    total = 0
    categories = ["lexical", "syntactic", "semantic"]
    
    for cat in categories:
        file_path = os.path.join(BASE_DIR, f"{cat}_cleaned.txt")
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                count = len(f.readlines())
                print(f"{cat.capitalize()}: {count} samples")
                total += count
        else:
            print(f"{cat.capitalize()}: 0 samples (File missing)")
            
    print("-" * 47)
    print(f"Total Cleaned Samples: {total}")
    print("-----------------------------------------------")

if __name__ == "__main__":
    generate_report()
