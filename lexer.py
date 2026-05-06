import re

# Tipos de tokens
KEYWORDS = {"rule", "if", "then", "AND"}
OPERATORS = {">", "<", "=", ":"}


def tokenize(text):
    tokens = []

    # Separar por espacios y símbolos
    pattern = r"(\bAND\b|\brule\b|\bif\b|\bthen\b|[><=:]|[a-zA-Z_][a-zA-Z0-9_]*|\d+)"
    matches = re.findall(pattern, text)

    for match in matches:
        if match in KEYWORDS:
            tokens.append(("KEYWORD", match))
        elif match in OPERATORS:
            tokens.append(("OPERATOR", match))
        elif match.isdigit():
            tokens.append(("NUMBER", int(match)))
        else:
            tokens.append(("IDENTIFIER", match))

    return tokens
