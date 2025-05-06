"""
Python program to replace all occurrences of a substring with another substring.
"""

# using replace()
def replace_substring(input_string, old_sub_string, new_sub_string):
    return input_string.replace(old_sub_string, new_sub_string)

str1 = "Python is a good programming language. Python is fun"
str2 = "Python"
str3 = "Java"

print(replace_substring(str1, str2, str3))

# using split() and join()
def replace_substring_1(input_string, old_sub_string, new_sub_string):
    parts = input_string.split(old_sub_string)
    return new_sub_string.join(parts)

print(replace_substring_1(str1, str2, str3))