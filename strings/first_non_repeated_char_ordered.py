"""
Python program to find the first non-repeated character in a string using OrderedDict.
"""
from collections import OrderedDict


def first_non_repeated_char_ordered(input_string):
    freq_dict = OrderedDict()
    for char in input_string:
        freq_dict[char] = freq_dict.get(char, 0) + 1
    print(freq_dict)
    for char, count in freq_dict.items():
        if count == 1:
            return char

str1 = "harsh saxena"
print(first_non_repeated_char_ordered(str1))