"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
"""


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        for i in nums:
            if i != val:
                nums[k] = i
                k += 1
        nums[:] = nums[:k]
        return k


nums = [0,1,2,2,3,0,4,2]
val = 2
obj = Solution()
print(obj.removeElement(nums, val))
print(nums)