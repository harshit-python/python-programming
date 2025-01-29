"""
Given an array of integers and a number K, find the maximum sum of a subarray of size K.
"""


def max_sum_subarray(arr1, k):
    n = len(arr1)
    if n<k:
        return -1

    window_sum = sum(arr1[:k])
    max_sum = window_sum

    for i in range(n-k):
        window_sum = window_sum - arr1[i] + arr1[i+k]
        max_sum = max(max_sum, window_sum)

    return max_sum


arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 3
print(max_sum_subarray(arr1, k)) # Output: 27