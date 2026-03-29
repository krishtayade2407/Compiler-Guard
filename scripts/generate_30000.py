import os
import random

def generate_hyper_scale(filename, templates, target_count):
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

    types = ["int", "double", "float", "size_t", "uintptr_t", "struct Node*", "char***", "bool", "long long"]
    vars = ["ptr", "idx", "counter", "buffer", "head", "tail", "msg", "data", "offset"]
    files = ["main.c", "utils.h", "network.c", "parser.y", "lexer.l", "config.h"]
    
    new_samples = set()
    while len(new_samples) < needed:
        temp = random.choice(templates)
        f_name = random.choice(files)
        v1 = f"{random.choice(vars)}_{random.randint(100, 999)}"
        v2 = f"{random.choice(vars)}_{random.randint(100, 999)}"
        t1 = random.choice(types)
        t2 = random.choice(types)
        line = random.randint(1, 5000)
        col = random.randint(1, 120)
        addr = hex(random.randint(0x100000, 0xFFFFFF))
        
        s = temp.format(v1=v1, v2=v2, t1=t1, t2=t2, f=f_name, l=line, c=col, a=addr)
        new_samples.add(s + "\n")

    with open(path, "a") as f:
        f.writelines(list(new_samples))
    print(f"🚀 Scaled {filename} to {target_count} samples.")

# --- HYPER-SCALE TEMPLATES ---
lex_temps = [
    "{f}:{l}:{c}: error: stray '\\{l}' in program",
    "invalid suffix \"_err{l}\" on integer constant at {a}",
    "missing terminating {v1} character in {f}",
    "unknown escape sequence: '\\{v1}' at column {c}",
    "invalid digit \"{l}\" in octal constant",
    "multi-character character constant '{v1}' in {f}:{l}",
    "hexadecimal floating constant at {a} requires an exponent",
    "stray '@' in program near memory {a}"
]

syn_temps = [
    "{f}:{l}:{c}: error: expected ';' before '{v1}'",
    "expected ')' before '{v2}' in function context",
    "expected '{t1}' before identifier at line {l}",
    "expected expression before '{v1}' at {a}",
    "missing '}}' at end of input in {f}",
    "expected declaration specifiers before '{t1}'",
    "expected ':' before 'default' in switch at {l}",
    "{f}: error: expected identifier or '(' before '{v1}'"
]

sem_temps = [
    "error: conflicting types for function '{v1}' at {a}",
    "'{v1}' undeclared (first use in this function) in {f}",
    "assignment to '{t1}' from '{t2}' makes integer from pointer",
    "passing argument of '{v1}' makes pointer from integer without a cast",
    "invalid use of undefined type '{t1}' at {f}:{l}",
    "error: size of array '{v1}' is negative ({l})",
    "incompatible types when assigning to type '{t1}' from type '{t2}'",
    "invalid operands to binary operator at {a} (have '{t1}' and '{t2}')",
    "called object '{v1}' is not a function or function pointer at {l}"
]

generate_hyper_scale("lexical_cleaned.txt", lex_temps, 10000)
generate_hyper_scale("syntactic_cleaned.txt", syn_temps, 10000)
generate_hyper_scale("semantic_cleaned.txt", sem_temps, 10000)
