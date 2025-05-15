"""
Given a string s, find the length of the longest
substring
without repeating characters.
"""
from typing import Optional

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        seen = set()
        max_length = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])
            max_length = max(max_length, right-left+1)

        return max_length

s = "abcabcbb"
obj = Solution()
# print(obj.lengthOfLongestSubstring(s))


#using for loop
def longest_substring_without_repeating(
    input_string,
    get_substring: Optional[bool] = False
):
    char_index = {}
    max_string = None
    start = max_length = max_start = 0
    for i in range(len(input_string)):
        char = input_string[i]
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        char_index[char] = i
        if get_substring:
            if (i-start+1) > max_length:
                max_length = i-start+1
                max_start = start
            max_string = input_string[max_start: max_start+max_length]
        else:
            max_length = max(max_length, i-start+1)
    if get_substring:
        return max_length, max_string
    else:
        return max_length


str1 = "abcdabdcbda"
print(longest_substring_without_repeating(str1, get_substring=True))
