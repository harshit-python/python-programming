"""
Given an integer array nums, find a
subarray
that has the largest product, and return the product.
"""


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_product, min_product, result = nums[0]
        for num in nums:
            if num < 0:
                max_product, min_product = min_product, max_product

            max_product = max(max_product, max_product*num)
            min_product = min(min_product, min_product*num)

            result = max(max_product, result)

        return result

nums = [2,3,-2,4]
solution_obj = Solution()
max_product = solution_obj.maxProduct(nums)
print(max_product)