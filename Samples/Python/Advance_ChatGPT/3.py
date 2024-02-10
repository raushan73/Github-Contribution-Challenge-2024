# Program: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
def twoSum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[num] = i

# Test case
arr = [2, 7, 11, 15]
target = 9
print(twoSum(arr, target))  # Expected output: [0, 1]
