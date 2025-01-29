"""
Given an array of positive numbers and a positive number S,
find the length of the smallest contiguous subarray whose sum is greater than or equal to S.
"""

def smallest_subarray_with_given_sum(arr1, sum1):
    window_sum = 0
    window_start = 0
    min_length = float("inf")

    for window_end in range(len(arr1)):
        window_sum += arr1[window_end]

        while window_sum >= sum1:
            min_length = min(min_length, window_end-window_start+1)
            window_sum-=arr1[window_start]
            window_start += 1

    return min_length



arr1 = [2, 1, 5, 2, 8]
sum1 = 7
print(smallest_subarray_with_given_sum(arr1, sum1)) # Output: 1