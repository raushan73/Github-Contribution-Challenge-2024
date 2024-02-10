# This program checks if a number is a prime number.

def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

# Bug: Incorrect condition in range
def is_prime_fixed(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n//2):  # Fix: changed range upper limit
            if n % i == 0:
                return False
        return True

if __name__ == "__main__":
    num = 17
    if is_prime_fixed(num):
        print(num, "is a prime number.")
    else:
        print(num, "is not a prime number.")
