"""
Given a string, find the length of the longest substring without repeating characters.
"""

def longest_substring(str1):
    n = len(str1)
    char_set = set()
    start = 0
    max_len = 0
    for end in range(n):
        while str1[end] in char_set:
            char_set.remove(str1[start])
            start += 1
        char_set.add(str1[end])
        max_len = max(max_len, end-start+1)

    return max_len


# program to return longest_substring

def return_longest_substring(arr1):
    max_len = 0
    max_substring = ""
    char_set = set()
    start = 0
    for end in range(len(arr1)):
        while arr1[end] in char_set:
            char_set.remove(arr1[start])
            start += 1

        char_set.add(str1[end])
        current_len = end - start + 1
        if current_len > max_len:
            max_len = current_len
            max_substring = str1[start:end+1]

    return max_substring

str1 = "abcabcbb"
print(longest_substring(str1))
print(return_longest_substring(str1))