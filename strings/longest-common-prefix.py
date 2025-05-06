"""
Python program to find the longest common prefix among a list of strings.
"""

def longest_common_prefix(strs):
    prefix = strs[0]
    for string in strs[1:]:
        while not string.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""

    return prefix


words = ["flower", "flow", "flight"]
print(longest_common_prefix(words))