"""
Write a python program to check number of vowels in a given string
"""

vowels = "aeiou"

# using for loop
def check_vowels(input_string):
    count = 0
    for s in input_string:
        if s in vowels:
            count += 1
    return count

str1 = "Harsh Saxena"
print(check_vowels(str1))


# using list comprehension
def check_vowels_1(input_string):
    return sum(1 for char in input_string if char in vowels)

print(check_vowels_1(str1))