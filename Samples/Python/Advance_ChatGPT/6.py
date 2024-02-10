# Program: Given an array of integers nums and an integer k, return the maximum sum of a contiguous subarray of size k.
def maxSubArray(nums, k):
    max_sum = float('-inf')
    window_sum = 0
    for i in range(len(nums) - k + 1):
        window_sum = sum(nums[i:i + k])
        max_sum = max(max_sum, window_sum)
    return max_sum

# Test case
arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
print(maxSubArray(arr, k))  # Expected output: 33
