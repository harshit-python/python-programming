"""
Python program to find the common characters between two strings:
"""

# using ser intersection
def common_characters(str1, str2):
    set1 = set(str1)
    set2 = set(str2)
    common_set = set1 & set2
    return "".join(common_set)

str1 = "harsh"
str2 = "harshit"
print(common_characters(str1, str2))


# using list comprehension for loop
def common_characters_1(str1, str2):
    return "".join([item for item in set(str1) if item in str2])
print(common_characters_1(str1, str2))
