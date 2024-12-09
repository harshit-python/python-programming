"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and using only constant extra space.
"""

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count_dict = {}
        for num in nums:
            if num in count_dict:
                count_dict[num] = count_dict[num] + 1
            else:
                count_dict[num] = 1
        for item in count_dict:
            if count_dict[item] > 1:
                return item



nums = [1,3,4,2,2]
solution_obj = Solution()
duplicate_number = solution_obj.findDuplicate(nums)
print(duplicate_number)

