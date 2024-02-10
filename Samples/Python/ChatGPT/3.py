# This program generates the Fibonacci sequence up to a specified number.

def generate_fibonacci(n):
    fib_sequence = [0, 1]
    while fib_sequence[-1] < n:
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)
    return fib_sequence

# Bug: Incorrect condition in while loop
def generate_fibonacci_fixed(n):
    fib_sequence = [0, 1]
    while fib_sequence[-1] <= n:  # Fix: changed < to <=
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)
    return fib_sequence

if __name__ == "__main__":
    num = 50
    fib_sequence = generate_fibonacci_fixed(num)
    print("Fibonacci sequence up to", num, ":", fib_sequence)
