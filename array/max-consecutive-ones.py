"""
Given a binary array nums, return the maximum number of consecutive 1s in the array.
"""


def max_consecutive_ones(arr1):
    max_ones = 0
    count = 0
    for i in arr1:
        if i == 1:
            count += 1
            max_ones = max(max_ones, count)
        else:
            count = 0

    return max_ones


arr1 = [1,1,1,0,0,1,1]
print(max_consecutive_ones(arr1))