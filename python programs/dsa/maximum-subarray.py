"""
Given an integer array nums, find the
subarray
with the largest sum, and return its sum.
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        print(nums)
        current_sum = max_sum = nums[0]
        for num in nums[1:]:
            current_sum = max(num, current_sum+num)
            max_sum = max(current_sum, max_sum)

        return max_sum



nums = [-2,1,-3,4,-1,2,1,-5,4]
solution_obj = Solution()
max_sum = solution_obj.maxSubArray(nums)
print(max_sum)