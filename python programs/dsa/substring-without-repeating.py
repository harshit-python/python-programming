"""
Given a string s, find the length of the longest
substring
without repeating characters.
"""

def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    left = 0
    max_length = 0
    char_set = set()
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left +=1
        char_set.add(s[right])
        max_length = max(max_length, (right-left+1))
    return max_length

string1 = "abcabcbb"
print(lengthOfLongestSubstring(string1))