import os
path = os.path.expanduser("~/CD_Lab_Project/data/cleaned_data/lexical_cleaned.txt")
with open(path, "r") as f:
    lines = list(set(f.readlines()))

new_variants = []
# Generate variations of stray characters (common in copy-paste errors)
for i in range(200, 260):
    new_variants.append(f"stray '\\{i}' in program\n")
# Generate variations of bad suffixes
for suffix in ["abc", "xyz", "fgh", "123L", "LLx"]:
    new_variants.append(f"invalid suffix \"{suffix}\" on integer constant\n")

with open(path, "a") as f:
    f.writelines(new_variants)
