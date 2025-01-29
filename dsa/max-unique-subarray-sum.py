"""
Return the maximum sum out of all almost unique subarrays of length k of nums. If no such subarray exists, return 0.
A subarray of nums is almost unique if it contains at least m distinct elements.
"""

def max_unique_subarray_sum(nums, k, m):
    max_sum = 0
    i = 0
    while len(nums)>=k:
        current_window = nums[i:k]
        if len(set(current_window)) >= m:
            max_sum = max(max_sum, sum(current_window))
        nums.pop(i)

    return max_sum

list1 = [5,9,9,2,4,5,4]
m = 1
k = 3
print(max_unique_subarray_sum(list1, k, m))