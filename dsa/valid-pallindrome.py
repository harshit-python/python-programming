"""
Python program to check whether given string is pallindrome or not
"""
from curses.ascii import isalnum


def check_pallindrome(
    str1
):
    """
    :param str1:
    :return:
    """
    updated_str = ''.join(char.lower() for char in str1 if char.isalnum())
    reversed_str = updated_str[::-1]
    if updated_str == reversed_str:
        return True
    else:
        return False



str1 = "a11 a"
print(check_pallindrome(str1))