"""
Write a python program to convert int to roman
"""

def int_to_roman(num):
    roman_dict = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    roman_sym = ""
    for value, symbol in roman_dict:
        while num >= value:
            roman_sym += symbol
            num -= value

    return roman_sym


num = 3749
print(int_to_roman(num))