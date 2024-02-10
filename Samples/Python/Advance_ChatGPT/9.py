# Program: Implement binary search algorithm to find the index of a target element in a rotated sorted array nums.
def search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] >= nums[left]:
            if target >= nums[left] and target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if target <= nums[right] and target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

    return -1

# Test case
arr = [4, 5, 6, 7, 0, 1, 2]
target = 0
print(search(arr, target))  # Expected output: 4
