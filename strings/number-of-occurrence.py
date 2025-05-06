"""
Python program to count the number of occurrences of a specific substring in a string.
"""
from itertools import count


# using find()
def number_of_occurrence(input_string, sub_string):
    index = 0
    count = 0
    while index < len(input_string):
        index = input_string.find(sub_string, index)
        if index == -1:
            break
        count += 1
        index += len(sub_string)
    return count

str1 = "Harsh Saxena is a Python Developer. He codes in Python"
str2 = "Python"
print(number_of_occurrence(str1, str2))


# using count()
def number_of_occurrence_1(input_string, sub_string):
    return input_string.count(sub_string)

print(number_of_occurrence_1(str1, str2))
