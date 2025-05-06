"""
Program to check if the given string is a valid palindrome or not
"""

def check_palindrome(input_string):
    return input_string.lower() == input_string[::-1].lower()

str1 = "Malayalam"
print(check_palindrome(str1))


# alternate

def check_palindrome_1(input_string):
    left, right = 0, len(input_string) - 1
    while left < right:
        if input_string[left].lower() != input_string[right].lower():
            return False
        left += 1
        right -= 1
    return True

print(check_palindrome_1(str1))


# using recursion

def check_palindrome_2(input_string):
    input_string = input_string.lower()
    if len(input_string) <= 1:
        return True
    if input_string[0] != input_string[-1]:
        return False
    return check_palindrome_2(input_string[1:-1])

print(check_palindrome_2(str1))
