"""
Write a function to find the longest common prefix string amongst an array of strings.
"""

def longest_common_prefix(strs):
    prefix = strs[0]
    for str in strs[1:]:
        while str[:len(prefix)] != prefix:
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix





strs = ["flower","flow","flight"]
print(longest_common_prefix(strs))