"""
Python program to reverse a given string
"""

# using slicing
def reverse_string(input_string):
    return input_string[::-1]

str1 = "harsh saxena"
print(reverse_string(str1))


# using for loop
def reverse_string_1(input_string):
    input_string = input_string.lower()
    reversed_string = ""
    for char in input_string:
        reversed_string = char + reversed_string
    return reversed_string

print(reverse_string_1(str1))


# using reversed
def reverse_string_2(input_string):
    return "".join(reversed(input_string))

print(reverse_string_2(str1))


# using recursion
def reverse_string_recursion(input_string):
    print(input_string)
    if len(input_string) <= 1:
        return input_string
    return reverse_string_recursion(input_string[1:]) + input_string[0]

print(reverse_string_recursion(str1))
