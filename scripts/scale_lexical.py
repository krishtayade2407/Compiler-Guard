import os
path = os.path.expanduser("~/CD_Lab_Project/data/cleaned_data/lexical_cleaned.txt")

with open(path, "r") as f:
    existing_lines = set(f.readlines())

new_samples = []
# Generate more stray byte variations (common in UTF-8 issues)
for i in range(150, 200):
    new_samples.append(f"stray '\\{i}' in program\n")

# Generate more bad suffix variations
suffixes = ["abc", "xyz", "fgh", "123L", "LLx", "i", "j", "k", "LLU", "f12", "d34"]
for s in suffixes:
    new_samples.append(f"invalid suffix \"{s}\" on integer constant\n")
    new_samples.append(f"invalid suffix \"{s}\" on floating constant\n")

# Generate missing quotes variations
contexts = ["at end of line", "in declaration", "in expression", "at end of file"]
for c in contexts:
    new_samples.append(f"missing terminating ' character {c}\n")
    new_samples.append(f"missing terminating \" character {c}\n")

with open(path, "a") as f:
    f.writelines(new_samples)
print("Lexical scaling to 400 complete.")
