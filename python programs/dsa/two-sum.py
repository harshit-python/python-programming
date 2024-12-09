# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                sum = nums[i] + nums[j]
                if sum == target:
                    return i, j
        return None

solution_obj = Solution()
index1, index2 = solution_obj.twoSum([3,2,3], 6)
print(index1, index2)