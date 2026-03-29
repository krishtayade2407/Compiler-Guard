import os

def generate_bulk(filename, templates, target_count):
    path = os.path.expanduser(f"~/CD_Lab_Project/data/cleaned_data/{filename}")
    
    # Load existing to avoid duplicates
    if os.path.exists(path):
        with open(path, "r") as f:
            existing = set(f.readlines())
    else:
        existing = set()

    current_count = len(existing)
    needed = target_count - current_count
    
    if needed <= 0:
        print(f"{filename} already has {current_count} samples.")
        return

    new_samples = set()
    types = ["int", "char", "float", "double", "long", "short", "void", "struct node", "struct student"]
    vars = [f"var_{i}" for i in range(500)]
    
    while len(new_samples) < needed:
        for temp in templates:
            if len(new_samples) >= needed: break
            # Logic to fill templates
            v1, v2 = vars[len(new_samples) % 500], vars[(len(new_samples) + 1) % 500]
            t1, t2 = types[len(new_samples) % 9], types[(len(new_samples) + 1) % 9]
            
            s = temp.replace("{v1}", v1).replace("{v2}", v2).replace("{t1}", t1).replace("{t2}", t2)
            s = s.replace("{n}", str(len(new_samples)))
            new_samples.add(s + "\n")

    with open(path, "a") as f:
        f.writelines(list(new_samples))
    print(f"Scaled {filename} to {target_count} samples.")

# --- TEMPLATES ---
lex_temps = [
    "stray '\\{n}' in program",
    "invalid suffix \"s{n}\" on integer constant",
    "missing terminating {v1} character",
    "unknown escape sequence: '\\{v1}'",
    "invalid digit \"{n}\" in octal constant",
    "multi-character character constant '{v1}{v2}'"
]

syn_temps = [
    "expected ';' before '{v1}'",
    "expected ')' before '{v1}'",
    "expected '{t1}' before '{v1}'",
    "expected identifier before '{v1}'",
    "expected expression before '{v1}'",
    "missing '{v1}' at end of input",
    "expected declaration specifiers before '{v1}'"
]

sem_temps = [
    "conflicting types for '{v1}'",
    "'{v1}' undeclared (first use in this function)",
    "assignment to '{t1}' from '{t2}' makes integer from pointer",
    "passing argument {n} of '{v1}' makes pointer from integer",
    "invalid use of undefined type '{t1}'",
    "size of array '{v1}' is negative",
    "incompatible types when assigning to type '{t1}' from type '{t2}'"
]

generate_bulk("lexical_cleaned.txt", lex_temps, 1000)
generate_bulk("syntactic_cleaned.txt", syn_temps, 1000)
generate_bulk("semantic_cleaned.txt", sem_temps, 1000)
