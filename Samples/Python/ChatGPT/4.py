# This program implements a basic calculator.

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Undefined"

# Bug: Incorrect division logic
def divide_fixed(x, y):
    if y != 0:
        return x // y  # Fix: changed / to //
    else:
        return "Undefined"

if __name__ == "__main__":
    num1 = 10
    num2 = 2
    print("Addition:", add(num1, num2))
    print("Subtraction:", subtract(num1, num2))
    print("Multiplication:", multiply(num1, num2))
    print("Division:", divide_fixed(num1, num2))
