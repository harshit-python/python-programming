"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a
subarray
whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
"""

class MinimalSizeSubArraySum():
    def get_minimum_subarray(self, nums, target):
        left = 0
        current_sum = 0
        minimum_length = float("inf")
        for right in range(len(nums)):
            current_sum += nums[right]
            while current_sum >= target:
                minimum_length = min(minimum_length, (right-left+1))
                current_sum -= nums[left]
                left += 1
        return minimum_length if minimum_length != float("inf") else 0

nums = [2,3,1,2,4,3]
target = 7
obj = MinimalSizeSubArraySum()
result = obj.get_minimum_subarray(nums, target)
print(result)