import re

class StructuralAnalyzer:
    def __init__(self):
        self.patterns = {
            'FunctionDef': r'\w+\s+\w+\s*\(.*\)\s*\{',
            'Loop': r'\b(for|while|do)\b',
            'Branching': r'\b(if|else|switch)\b',
            'DataType': r'\b(int|float|char|double|void|struct)\b\s+\w+',
            'Return': r'\breturn\b',
            'Assignment': r'(?<!=)=(?!=)'
        }

    def extract_features(self, code):
        found_nodes = []
        if any(c in code for c in ['{', '}', ';', '(', ')']):
            for name, pattern in self.patterns.items():
                if re.search(pattern, code):
                    found_nodes.append(name)
        return found_nodes if found_nodes else ["Standalone Log"]
