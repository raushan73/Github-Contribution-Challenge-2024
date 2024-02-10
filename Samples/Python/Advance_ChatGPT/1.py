# Program: Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.
def removeDuplicates(nums):
    if len(nums) == 0:
        return 0

    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]

    return i + 1

# Test case
arr = [1, 1, 2]
print(removeDuplicates(arr))  # Expected output: 2
