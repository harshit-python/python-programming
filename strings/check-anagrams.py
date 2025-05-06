"""
Python program to check whether given 2 strings are anagrams of each other or not
"""


# using sorted
def check_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    return sorted(str1) == sorted(str2)

str1 = "silent"
str2 = "listen"
print(check_anagrams(str1, str2))

# using counter
from collections import Counter
def check_anagrams_1(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    return Counter(str1) == Counter(str2)

print(check_anagrams_1(str1, str2))