"""
Python program to reverse the order of words in a sentence.
"""

# using slicing
def reverse_order(input_string):
    words = input_string.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)

str1 = "harsh saxena is the python developer"
print(reverse_order(str1))

# using for loop
def reverse_order_1(input_string):
    reversed_words = []
    words = input_string.split()
    for char in range(len(words)-1, -1, -1):
        reversed_words.append(words[char])
    return " ".join(reversed_words)

print(reverse_order_1(str1))

# using reversed()
def reverse_order_2(input_string):
    words = input_string.split()
    reversed_words = reversed(words)
    return " ".join(reversed_words)

print(reverse_order_2(str1))
