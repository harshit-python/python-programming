"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1.
If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.
"""


class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i, j = 0, 0
        merged = []
        while i < len(word1) and j < len(word2):
            merged.append(word1[i])
            merged.append(word2[j])
            i += 1
            j += 1
        merged.append(word1[i:])
        merged.append(word2[j:])
        merged_string = "".join(merged)
        return merged_string

word1 = "abc"
word2 = "pqr"
obj = Solution()
merged_string = obj.mergeAlternately(word1, word2)
print("---merged string---", merged_string)