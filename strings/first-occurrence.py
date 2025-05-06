"""
Python program to find the index of the first occurrence of a substring in a string.
"""

# using find()
def first_occurrence(input_string, sub_string):
    return input_string.find(sub_string)

str1 = "Harsh Saxena is a Python Developer. He codes in Python"
str2 = "Python"
print(first_occurrence(str1, str2))


# using index()
def first_occurrence_1(input_string, sub_string):
    return input_string.index(sub_string)

str1 = "Harsh Saxena is a Python Developer. He codes in Python"
str2 = "Python"
print(first_occurrence_1(str1, str2))