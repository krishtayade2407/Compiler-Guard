import os

def mass_augment(filename, patterns):
    path = os.path.expanduser(f"~/CD_Lab_Project/data/cleaned_data/{filename}")
    new_data = []
    for p in patterns:
        for i in range(40): # Create 40 variations of each pattern
            new_data.append(p.replace("VAR", f"var_{i}").replace("TYPE", f"type_{i}") + "\n")
    
    with open(path, "a") as f:
        f.writelines(new_data)

# Semantic Variations
mass_augment("semantic_cleaned.txt", [
    "conflicting types for 'VAR'",
    "passing argument of 'VAR' makes pointer from integer",
    "assignment to 'TYPE' from 'TYPE' makes integer from pointer",
    "VAR undeclared (first use in this function)"
])

# Syntactic Variations
mass_augment("syntactic_cleaned.txt", [
    "expected ';' before 'VAR'",
    "expected ')' before 'VAR'",
    "expected identifier before 'VAR'",
    "stray 'VAR' in program"
])

print("Mass Augmentation Complete.")
