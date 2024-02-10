# Program: Implement binary search algorithm to find the index of a target element in a sorted array nums.
def binarySearch(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Test case
arr = [1, 2, 3, 4, 5]
target = 4
print(binarySearch(arr, target))  # Expected output: 3
