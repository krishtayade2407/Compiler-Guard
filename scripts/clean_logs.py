import os
import re

BASE_DIR = os.path.expanduser("~/CD_Lab_Project/data")
RAW_DIR = f"{BASE_DIR}/raw_logs"
CLEAN_DIR = f"{BASE_DIR}/cleaned_data"

def clean_error_text(text):
    # Remove file paths and line numbers 
    cleaned = re.sub(r'^.*?:\d+:\d+: ', '', text)
    # Remove "error: " prefix 
    cleaned = re.sub(r'^error: ', '', cleaned)
    return cleaned.strip()

def run_cleaning():
    print("Running Advanced Data Cleaning & Labeling...")
    os.makedirs(CLEAN_DIR, exist_ok=True)
    
    for cat in ["lexical", "syntactic", "semantic"]:
        raw_cat_path = os.path.join(RAW_DIR, cat)
        if not os.path.exists(raw_cat_path): continue
        
        cleaned_file_path = os.path.join(CLEAN_DIR, f"{cat}_cleaned.txt")
        
        with open(cleaned_file_path, "w") as outfile:
            for file_name in os.listdir(raw_cat_path):
                if file_name.endswith(".log"):
                    with open(os.path.join(raw_cat_path, file_name), "r") as f:
                        lines = f.readlines()
                        # Search for the line that actually has the error message 
                        for line in lines:
                            if "error:" in line:
                                clean_line = clean_error_text(line)
                                if clean_line:
                                    outfile.write(clean_line + "\n")
                                break # Stop after finding the first error 
        
        print(f"Refined clean data saved for: {cat}")

if __name__ == "__main__":
    run_cleaning()
