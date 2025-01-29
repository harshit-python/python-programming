"""
You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:

    The length of the subarray is k, and
    All the elements of the subarray are distinct.

Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.

A subarray is a contiguous non-empty sequence of elements within an array.
"""


class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        curr_sum = 0
        max_sum = 0
        left = 0
        seen = set()

        for right in range(len(nums)):
            while nums[right] in seen:
                seen.remove(nums[left])
                curr_sum -= nums[left]
                left += 1

            seen.add(nums[right])
            curr_sum += nums[right]

            if right - left + 1 == k:
                max_sum = max(curr_sum, max_sum)
                seen.remove(nums[left])
                curr_sum -= nums[left]
                left += 1

        return max_sum


nums = [1,5,4,2,9,9,9]
k = 3

obj = Solution()
max_sum = obj.maximumSubarraySum(nums, k)
print(f"max sum is: {max_sum}")
