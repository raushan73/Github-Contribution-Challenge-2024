# This program sorts a list of numbers using bubble sort algorithm.

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Bug: No return statement
def bubble_sort_fixed(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr  # Fix: added return statement

if __name__ == "__main__":
    numbers = [64, 34, 25, 12, 22, 11, 90]
    print("Original list:", numbers)
    sorted_numbers = bubble_sort_fixed(numbers)
    print("Sorted list:", sorted_numbers)
