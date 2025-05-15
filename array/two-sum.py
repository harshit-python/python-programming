"""
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to the target.
"""


def two_sum(arr1, target):
    num_to_index = {}
    for index, num in enumerate(arr1):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], index]
        num_to_index[num] = index


arr1 = [2, 7, 11, 15]
target = 9
print(two_sum(arr1, target))