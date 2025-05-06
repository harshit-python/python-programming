"""
Python program to find longest word in a given sentence
"""

# using for loop
def longest_word(input_string):
    input_string_list = input_string.split()
    longest = ''
    for word in input_string_list:
        if len(word) > len(longest):
            longest = word
    return longest

str1 = "Harsh Saxena is a Python developer"
print(longest_word(str1))


# using sorted()
def longest_word_1(input_string):
    input_string_list = input_string.split()
    sorted_list = sorted(input_string_list, key=len, reverse=True)
    return sorted_list[0]

print(longest_word_1(str1))

# using max
def longest_word_2(input_string):
    input_string_list = input_string.split()
    return max(input_string_list, key=len)

print(longest_word_2(str1))