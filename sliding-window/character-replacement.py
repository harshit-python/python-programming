"""
Given a string consisting of uppercase English letters, you can replace any letter with another letter at most k times.
Find the length of the longest substring containing the same letter after k replacements.
"""

from collections import defaultdict
from typing import Optional

def character_replacement(s:str, k:int, get_substring: Optional[bool] = False):
    count = defaultdict(int)
    max_count = 0
    max_len = 0
    start_index = 0

    left = 0
    for right in range(len(s)):
        count[s[right]] += 1

        max_count = max(max_count, count[s[right]])

        # if window is valid then shrink the window
        if right - left + 1 - max_count > k:
            count[s[left]] -= 1
            left += 1

        if get_substring:
            if right - left + 1 > max_len:
                # update max length
                max_len = right - left + 1
                start_index = left
        else:
            # update max length
            max_len = max(max_len, right - left + 1)
    if get_substring:
        return max_len, s[start_index: start_index + max_len]
    else:
        return max_len

str1 = "AABABBA"
k = 1
print(character_replacement(str1, k, get_substring=True))