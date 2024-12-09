"""
Given an integer array nums sorted in non-decreasing order,
remove some duplicates in-place such that each unique element appears at most twice.
The relative order of the elements should be kept the same.
"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        count = 1
        for j in range(1, len(nums)):
            if nums[j] == nums[j-1]:
                count += 1
            else:
                count = 1
            if count <= 2:
                nums[i] = nums[j]
                i+=1
        return i


nums = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4]
obj = Solution().removeDuplicates(nums)
print(obj)
print(nums)