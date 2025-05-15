"""
Given an array of integers nums and an integer k,
return the total number of continuous sub arrays whose sum equals to k.
"""

def subarray_sum(arr1, k):
    n = len(arr1)
    sum = 0
    count = 0
    sum_dict = {}
    for i in range(n):
        sum += 1
        if sum == k:
            count += 1
        if (sum-k) in sum_dict:
            count += sum_dict[sum - k]
        if sum in sum_dict:
            sum_dict[sum] += 1
        else:
            sum_dict[sum] = 1
    return count


arr1 = [1,1,1,-1]
print(subarray_sum(arr1, 2))