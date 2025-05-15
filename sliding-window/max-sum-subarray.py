"""
Given an array of integers and a number K, find the maximum sum of a subarray of size K.
"""
from typing import Optional


def max_sum_subarray(arr1, k, get_subarray: Optional[bool] = False):
    # checking whether a valid array
    if len(arr1)<k:
        return None

    # sum of first window
    window_sum = sum(arr1[:k])
    max_sum = window_sum
    max_start = 0

    for i in range(k, len(arr1)):
        window_sum = window_sum - arr1[i-k] + arr1[i]
        if get_subarray:
            if window_sum > max_sum:
                max_sum = window_sum
                max_start = i-k+1
        else:
            max_sum = max(window_sum, max_sum)

    if get_subarray:
        sub_array = arr1[max_start:max_start+k]
        return max_sum, sub_array
    else:
        return max_sum


arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 3
print(max_sum_subarray(arr1, k, get_subarray=True)) # Output: 27