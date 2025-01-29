"""
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
Each element nums[i] represents the maximum length of a forward jump from index i.
In other words, if you are at nums[i], you can jump to any nums[i + j]
Return the minimum number of jumps to reach nums[n - 1].
"""

def minimum_jumps(nums):
    max_reach = 0
    jump_count = 0
    current_jump_end = 0
    for i in range(len(nums)-1):
        max_reach = max(max_reach, i+nums[i])
        if i == current_jump_end:
            current_jump_end = max_reach
            jump_count += 1

            if current_jump_end >= len(nums)-1:
                return jump_count

    return jump_count

nums = [2,3,1,1,4]
# nums = [1,2,1,1,1]
# nums = [2,0,2,0,1]
print(minimum_jumps(nums))