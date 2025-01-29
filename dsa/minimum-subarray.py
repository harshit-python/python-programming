"""
Given an array of positive integers nums and a positive integer target, return the minimum subarray
whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
"""

class MinimumSubArraySum():
    def find_minimum_subarray(self, nums, target):
        left = 0
        current_sum = 0
        minimum_length = float("inf")
        result_subarray = []

        for right in range(len(nums)):
            current_sum += nums[right]
            while current_sum >= target:
                if right-left+1 < minimum_length:
                    minimum_length = right-left+1
                    result_subarray = nums[left:right+1]
                current_sum -= nums[left]
                left += 1

        if minimum_length == float("inf"):
            return 0, []
        else:
            return minimum_length, result_subarray



nums = [2,3,1,2,4,3]
target = 7
obj = MinimumSubArraySum()
result = obj.find_minimum_subarray(nums, target)
print(result)