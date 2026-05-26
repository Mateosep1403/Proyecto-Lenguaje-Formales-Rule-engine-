from ast_nodes import AndCondition, Comparison, Fact


def evaluate_condition(condition, variables, facts):

    # AND
    if isinstance(condition, AndCondition):

        return (
            evaluate_condition(
                condition.left,
                variables,
                facts
            )
            and
            evaluate_condition(
                condition.right,
                variables,
                facts
            )
        )

    # Comparaciones
    elif isinstance(condition, Comparison):

        identifier = condition.identifier
        operator = condition.operator
        value = condition.value

        if identifier not in variables:
            return False

        variable_value = variables[identifier]

        if operator == ">":
            return variable_value > value

        elif operator == "<":
            return variable_value < value

        elif operator == "=":
            return variable_value == value

    # Facts activos
    elif isinstance(condition, Fact):

        return condition.identifier in facts

    return False


def execute(program, variables, initial_facts):

    # Facts activos totales
    active_facts = set(initial_facts)

    # SOLO los generados por reglas
    generated_facts = set()

    changed = True

    while changed:

        changed = False

        new_facts = set()

        for rule in program.rules:

            if evaluate_condition(
                rule.condition,
                variables,
                active_facts
            ):

                action_fact = rule.action.identifier

                if action_fact not in active_facts:

                    new_facts.add(action_fact)

        if new_facts:

            active_facts.update(new_facts)

            generated_facts.update(new_facts)

            changed = True

    # Retornar SOLO los nuevos facts
    return sorted(generated_facts)