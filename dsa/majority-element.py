"""
Given an array nums of size n, return the majority element.
"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate = None
        count = 0
        for i in nums:
            if count == 0:
                candidate = i
            if candidate == i:
                count += 1
            else:
                count -= 1
        return candidate



nums = [2,2,1,4,4,4,4,4,4,4,1,1,2,2]
obj = Solution().majorityElement(nums)
print(nums)
print(obj)