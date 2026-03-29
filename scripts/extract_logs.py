import subprocess
import os

# Use the GCC version we just installed via Homebrew
COMPILER = "gcc-15" 
BASE_DIR = os.path.expanduser("~/CD_Lab_Project/data")
CATEGORIES = ["lexical", "syntactic", "semantic"]

def run_extraction():
    print(f"Starting log extraction using {COMPILER}...")
    for cat in CATEGORIES:
        code_path = f"{BASE_DIR}/code_snippets/{cat}"
        log_path = f"{BASE_DIR}/raw_logs/{cat}"
        
        # Phase 3 requirement: Create directory for raw logs [cite: 54, 62]
        os.makedirs(log_path, exist_ok=True)

        if not os.path.exists(code_path):
            print(f"Directory not found: {code_path}")
            continue

        for file in os.listdir(code_path):
            if file.endswith(".c"):
                input_file = os.path.join(code_path, file)
                output_log = os.path.join(log_path, f"{file}.log")
                
                # Activity: Capture build logs/error messages [cite: 58]
                # -c tells GCC to compile but not link
                result = subprocess.run([COMPILER, "-c", input_file], capture_output=True, text=True)
                
                with open(output_log, "w") as f:
                    # result.stderr contains the compiler's error message
                    f.write(result.stderr)
                print(f"Successfully captured: {output_log}")

if __name__ == "__main__":
    run_extraction()
