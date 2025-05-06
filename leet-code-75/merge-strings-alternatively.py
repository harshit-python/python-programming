"""
You are given two strings word1 and word2.
Merge the strings by adding letters in alternating order, starting with word1.
If a string is longer than the other, append the additional letters onto the end of the merged string.
"""


class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged = []
        len1 = len(word1)
        len2 = len(word2)
        min_length = min(len1, len2)
        for i in range(min_length):
            merged.append(word1[i])
            merged.append(word2[i])
        if len1 > len2:
            merged.append(word1[min_length:])
        else:
            merged.append(word2[min_length:])
        return "".join(merged)


obj1 = Solution()
word1 = "abc"
word2 = "pqrstuv"
print(obj1.mergeAlternately(word1 = word1, word2 = word2))