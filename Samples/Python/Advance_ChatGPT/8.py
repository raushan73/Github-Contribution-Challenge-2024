# Program: Given a sorted array nums, remove the target element in-place and return the new length.
def removeElement(nums, target):
    i = 0
    for j in range(len(nums)):
        if nums[j] != target:
            nums[i] = nums[j]
            i += 1
    return i

# Test case
arr = [3, 2, 2, 3]
target = 3
print(removeElement(arr, target))  # Expected output: 2
