"""
Given two strings s and t, find the minimum window in s which will contain all the characters in t.
"""
from collections import Counter


def minimum_window_substring(s, t):
    left = 0
    t_count = Counter(t)
    required = len(t_count)
    window_count = {}
    formed = 0
    min_len = float("inf")
    min_window = (0,0)

    for right in range(len(s)):
        char = s[right]
        window_count[char] = window_count.get(char, 0) + 1
        if char in t_count and window_count[char] == t_count[char]:
            formed += 1
        if formed == required:
            # update minimum window
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_window = (left, right)

            # shrink the window
            left_char = s[left]
            window_count[left_char] -= 1
            if window_count[left_char] < t_count[left_char]:
                formed -= 1
    l, r = min_window
    return s[l:r+1] if min_len != float("inf") else ""



s = "harsh"
t = "har"
print(minimum_window_substring(s, t))