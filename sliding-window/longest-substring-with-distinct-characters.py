"""
Given a string, find the length of the longest substring in it with at most K distinct characters.
"""

def longest_substring_with_k_distinct(s, k):
    max_length = 0
    window_start = 0
    char_freq = {}

    for window_end in range(len(s)):
        right_char = s[window_end]
        if right_char not in char_freq:
            char_freq[right_char] = 0
        char_freq[right_char] += 1

        while len(char_freq) > k:
            left_char = s[window_start]
            char_freq[left_char] -= 1
            if char_freq[left_char] == 0:
                del char_freq[left_char]
            window_start += 1

        max_length = max(max_length, window_end-window_start+1)

    return max_length




# Example usage
s = "araaci"
k = 2
print(longest_substring_with_k_distinct(s, k)) # Output: 4