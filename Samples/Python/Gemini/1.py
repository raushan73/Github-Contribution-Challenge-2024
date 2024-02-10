# Calculates the factorial of a number (but has errors)

def factorial(n):
    """Calculates the factorial of a non-negative integer n.

    Args:
        n: The non-negative integer for which to calculate the factorial.

    Returns:
        The factorial of n.
    """

    if n < 0:  # Incorrect base case (should be non-negative)
        return "Factorial is not defined for negative numbers"
    else:
        result = 1
        while n > 0:  # Missing decrement (infinite loop)
            result *= n
        return result

# Example usage
number = 5
factorial_result = factorial(number)
print(f"The factorial of {number} is {factorial_result}")
