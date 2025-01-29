"""
Given an integer array nums sorted in non-decreasing order,
remove the duplicates in-place such that each unique element appears only once.
The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for j in range(1, len(nums)):
            if nums[j]!= nums[i]:
                i += 1
                nums[i] = nums[j]
        del nums[i+1:]

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
obj = Solution().removeDuplicates(nums)
print(nums)