"""
Write a python program to convert roman to int
"""


def roman_to_int(sym):
    total_sum = 0
    prev_value = 0
    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    for char in reversed(sym):
        current_value = roman_dict[char]
        if current_value < prev_value:
            total_sum -= current_value
        else:
            total_sum += current_value
        prev_value = current_value

    return total_sum

sym = "LVIII"
print(roman_to_int(sym))
