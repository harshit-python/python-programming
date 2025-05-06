"""
Python program to find if a given string contains only digits
"""

# using isdigit()
def check_only_digits(input_string):
    return input_string.isdigit()

str1 = "3535315"
print(check_only_digits(str1))


# using for loop
def check_only_digits_1(input_string):
    for char in input_string:
        if char < "0" or char > "9":
            return False
    return True

str2 = "3532210"
print(check_only_digits_1(str2))