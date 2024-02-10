# Simple calculator with various potential errors

def calculate(expression):
    """Evaluates a mathematical expression.

    Args:
        expression: The mathematical expression to evaluate.

    Returns:
        The result of the evaluation.
    """

    try:
        # Potential errors:
        # - Incorrect operator precedence (e.g., not using PEMDAS)
        # - Division by zero
        # - Missing parentheses
        # - Invalid operators or operands
        result = eval(expression)
        return result
    except Exception as e:  # Generic exception handling (could be more specific)
        return "Invalid expression"

# Example usage
expression = "(5 + 3) * 2 / 0"  # Division by zero error and potentially others
result =
