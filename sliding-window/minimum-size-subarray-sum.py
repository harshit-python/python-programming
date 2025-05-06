"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a
subarray
whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
"""

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        min_length = float('inf')
        curr_sum = 0

        for right in range(len(nums)):
            curr_sum+=nums[right]
            while curr_sum >= target:
                min_length = min(min_length, right-left+1)
                curr_sum -= nums[left]
                left+=1
        return curr_sum if curr_sum != float('inf') else 0

nums = [2,3,1,2,4,3]
target = 7
obj = Solution()
print(obj.minSubArrayLen(target, nums))