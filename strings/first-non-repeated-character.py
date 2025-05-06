"""
Python program to find the first non-repeated character in a string
"""

# using for loop
def first_non_repeated_char(input_string):
    for char in input_string:
        if input_string.count(char) == 1:
            return char

    return None

str1 = "harsh"
print(first_non_repeated_char(str1))

# using dictionary
def first_non_repeated_char_1(input_string):
    count_dict = {}
    for char in input_string:
        count_dict[char] = count_dict.get(char, 0) + 1
    for item in count_dict.items():
        if item[1] == 1:
            return item[0]

print(first_non_repeated_char_1(str1))