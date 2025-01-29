"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
"""

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        # reversing whole list
        self.reverse(nums, 0, n-1)
        # reversing first k elements
        self.reverse(nums, 0, k-1)
        # reversing remaining elements
        self.reverse(nums, k, n-1)
        return nums

    def reverse(self, nums, start, end):
        while start<end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


nums = [1,2,3,4,5,6,7]
k = 3
obj = Solution().rotate(nums,k)
print(obj)
