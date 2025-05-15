"""
Given an array nums, there is a sliding window of size k which moves from the very left to the very right of the array.
 You can only see the k numbers in the window. Find the maximum in each sliding window.
"""
from collections import deque


def maximum_sliding_window(nums, k):
    if not nums or k == 0:
        return []

    dq = deque()
    result = []

    for i in range(len(nums)):

        # remove the indices that are out of the window
        if dq and dq[0] < i - k + 1:
            dq.popleft()

        # remove the indices whose values are less than the current value
        while dq and nums[dq[-1]] <= nums[i]:
            dq.pop()

        dq.append(i)

        # record the maximum when first window is complete
        if i>=k-1:
            result.append(nums[dq[0]])

    return result


nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(maximum_sliding_window(nums, k))