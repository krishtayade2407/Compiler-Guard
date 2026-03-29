import os

def augment(filename, variations):
    path = os.path.expanduser(f"~/CD_Lab_Project/data/cleaned_data/{filename}")
    with open(path, "r") as f:
        lines = list(set(f.readlines())) # unique lines
    
    new_lines = []
    for line in lines:
        for v in variations:
            # Simple replacement logic to create variations
            nl = line.replace("'int'", v).replace("'char'", v)
            new_lines.append(nl)
    
    with open(path, "a") as f:
        f.writelines(new_lines[:150]) # Add enough to reach target

augment("semantic_cleaned.txt", ["'float'", "'double'", "'struct node'", "'void'"])
augment("syntactic_cleaned.txt", ["'while'", "'for'", "'switch'", "'if'"])
print("Data Augmentation complete. Checking totals...")
