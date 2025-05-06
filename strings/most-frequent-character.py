"""
Python program to find most frequent character in the provided string
"""

# Using a dictionary
def most_frequent_char(input_string):
    input_string = input_string.lower().replace(" ", "")
    freq = {}
    for s in input_string:
        freq[s] = freq.get(s, 0) + 1
    return max(freq, key=freq.get), freq[max(freq, key=freq.get)]

str1 = "Harsh saxena"
print(most_frequent_char(str1))


# Using Counter
from collections import Counter
def most_freq_char_counter(input_string):
    input_string = input_string.lower().replace(" ", "")
    counter = Counter(input_string)
    return counter.most_common(1)[0] if counter.most_common(1) else (None, 0)

print("=============")
print("using counter")
print(most_freq_char_counter(str1))