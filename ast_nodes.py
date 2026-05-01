class Program:
    def __init__(self, rules):
        self.rules = rules


class Rule:
    def __init__(self, name, condition, action):
        self.name = name
        self.condition = condition
        self.action = action


class Condition:
    pass


class AndCondition(Condition):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Comparison(Condition):
    def __init__(self, identifier, operator, value):
        self.identifier = identifier
        self.operator = operator
        self.value = value


class Fact(Condition):
    def __init__(self, identifier):
        self.identifier = identifier


class Action:
    def __init__(self, identifier):
        self.identifier = identifier