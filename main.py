from lexer import tokenize
from parser import Parser


def read_input(filename):
    with open(filename, "r") as file:
        content = file.read()

    parts = content.split("---")

    rules_part = parts[0].strip()
    state_part = parts[1].strip() if len(parts) > 1 else ""

    return rules_part, state_part


def parse_state(state_text):
    variables = {}
    facts = set()

    lines = state_text.split("\n")

    for line in lines:
        line = line.strip()
        if not line:
            continue

        if "=" in line:
            name, value = line.split("=")
            variables[name.strip()] = int(value.strip())
        else:
            facts.add(line)

    return variables, facts


if __name__ == "__main__":
    rules_text, state_text = read_input("input.txt")

    tokens = tokenize(rules_text)

    parser = Parser(tokens)
    program = parser.parse_program()

    print("=== REGLAS PARSEADAS ===")
    for rule in program.rules:
        print(f"Rule: {rule.name} -> Action: {rule.action.identifier}")
