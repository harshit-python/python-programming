"""
Python program to check if a string contains only unique characters.
"""

# using dictionary
def has_unique_characters(input_string):
    freq_dict = {}
    for char in input_string:
        freq_dict[char] = freq_dict.get(char, 0) + 1
    print(freq_dict)
    return all(value==1 for value in freq_dict.values())

str1 = "harsh saxena"
print(has_unique_characters(str1))


# using counter
from collections import Counter

def has_unique_characters_1(input_string):
    counter_obj = Counter(input_string)
    print(counter_obj)
    return all(value==1 for value in counter_obj.values())

print(has_unique_characters_1(str1))