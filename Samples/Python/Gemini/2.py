# Calculates the average of elements in a list (with errors)

def calculate_average(numbers):
    """Calculates the average of a list of numbers.

    Args:
        numbers: A list of numbers.

    Returns:
        The average of the numbers in the list.
    """

    total = 0
    for num in numbers:  # Assumes elements are numerical (potential type error)
        total += num
    average = total / len(numbers)
    return average

# Example usage
data = ["5", 3, 7.2, 1]  # Mixing strings and numbers in the list
average_value = calculate_average(data)
print(f"The average of the numbers is {average_value}")
