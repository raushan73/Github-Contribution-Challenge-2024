# This program calculates the average of a list of numbers.

def calculate_average(numbers):
    total = sum(numbers)
    return total / len(numbers)

# Bug: Incorrect function name
def calc_average(numbers):
    total = sum(numbers)
    return total / len(numbers)

if __name__ == "__main__":
    numbers = [10, 20, 30, 40, 50]
    avg = calc_average(numbers)
    print("Average:", avg)
