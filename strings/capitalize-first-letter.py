"""
Python program to capitalize first word of each letter in a given sentence
"""

def capitalize_first_word(input_string):
    input_string_list = input_string.split()
    result = [char.capitalize() for char in input_string_list]
    return " ".join(result)

str1 = "My name is harsh saxena"
print(capitalize_first_word(str1))