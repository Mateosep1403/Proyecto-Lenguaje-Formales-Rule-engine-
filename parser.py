from ast_nodes import *


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def eat(self, expected_type=None, expected_value=None):
        token = self.current()

        if token is None:
            raise Exception("Unexpected end of input")

        token_type, token_value = token

        if expected_type and token_type != expected_type:
            raise Exception(f"Expected type {expected_type}, got {token_type}")

        if expected_value and token_value != expected_value:
            raise Exception(f"Expected value {expected_value}, got {token_value}")

        self.pos += 1
        return token_value

    def parse_program(self):
        rules = []

        while self.current() is not None:
            rules.append(self.parse_rule())

        return Program(rules)

    def parse_rule(self):
        self.eat("KEYWORD", "rule")
        name = self.eat("IDENTIFIER")
        self.eat("OPERATOR", ":")
        self.eat("KEYWORD", "if")

        condition = self.parse_condition()

        self.eat("KEYWORD", "then")
        action_id = self.eat("IDENTIFIER")

        return Rule(name, condition, Action(action_id))

    def parse_condition(self):
        left = self.parse_atom()

        while self.current() and self.current()[1] == "AND":
            self.eat("KEYWORD", "AND")
            right = self.parse_atom()
            left = AndCondition(left, right)

        return left

    def parse_atom(self):
        identifier = self.eat("IDENTIFIER")

        if self.current() and self.current()[0] == "OPERATOR" and self.current()[1] in [">", "<", "="]:
            op = self.eat("OPERATOR")
            value = self.eat("NUMBER")
            return Comparison(identifier, op, value)

        return Fact(identifier)