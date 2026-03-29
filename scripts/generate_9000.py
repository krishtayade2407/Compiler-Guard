import os
import random

def generate_grand_scale(filename, templates, target_count):
    path = os.path.expanduser(f"~/CD_Lab_Project/data/cleaned_data/{filename}")
    
    if os.path.exists(path):
        with open(path, "r") as f:
            existing = set(f.readlines())
    else:
        existing = set()

    needed = target_count - len(existing)
    if needed <= 0:
        print(f"{filename} already has {len(existing)} samples.")
        return

    # Expanded dictionaries for diversity
    types = ["int", "char", "float", "double", "long", "short", "void", "size_t", "ssize_t", "uint32_t", "struct Node", "FILE*", "char**"]
    std_funcs = ["printf", "scanf", "malloc", "free", "memcpy", "strlen", "fopen", "main", "exit"]
    operators = ["+", "-", "*", "/", "%", "==", "!=", "&&", "||", "<<", ">>"]
    
    new_samples = set()
    while len(new_samples) < needed:
        temp = random.choice(templates)
        v1 = f"var_{random.randint(1000, 9999)}"
        v2 = f"ptr_{random.randint(1000, 9999)}"
        t1 = random.choice(types)
        t2 = random.choice(types)
        f1 = random.choice(std_funcs)
        op = random.choice(operators)
        num = random.randint(0, 10000)
        
        s = temp.format(v1=v1, v2=v2, t1=t1, t2=t2, f1=f1, op=op, n=num)
        new_samples.add(s + "\n")

    with open(path, "a") as f:
        f.writelines(list(new_samples))
    print(f"Successfully scaled {filename} to {target_count} samples.")

# --- DIVERSE TEMPLATES ---
lex_temps = [
    "stray '\\{n}' in program",
    "invalid suffix \"s{n}\" on integer constant",
    "missing terminating {v1} character",
    "unknown escape sequence: '\\{v1}'",
    "invalid digit \"{n}\" in octal constant",
    "multi-character character constant '{v1}'",
    "invalid suffix \"{v1}\" on floating constant",
    "stray '@' in program code near {v1}",
    "null character(s) preserved in literal {v1}"
]

syn_temps = [
    "expected ';' before '{v1}'",
    "expected ')' before '{v2}'",
    "expected '{t1}' before '{f1}'",
    "expected identifier before '{op}'",
    "expected expression before '{v1}'",
    "missing '{t1}' at end of input in {f1}",
    "expected declaration specifiers before '{v2}'",
    "expected ':' before 'default' in {f1}",
    "expected 'while' before '(' in loop {v1}"
]

sem_temps = [
    "conflicting types for '{f1}'",
    "'{v1}' undeclared (first use in this function)",
    "assignment to '{t1}' from '{t2}' makes integer from pointer",
    "passing argument {n} of '{f1}' makes pointer from integer without a cast",
    "invalid use of undefined type '{t1}' in {v1}",
    "size of array '{v1}' is negative",
    "incompatible types when assigning to type '{t1}' from type '{t2}'",
    "invalid operands to binary {op} (have '{t1}' and '{t2}')",
    "called object '{v1}' is not a function or function pointer"
]

generate_grand_scale("lexical_cleaned.txt", lex_temps, 3000)
generate_grand_scale("syntactic_cleaned.txt", syn_temps, 3000)
generate_grand_scale("semantic_cleaned.txt", sem_temps, 3000)
