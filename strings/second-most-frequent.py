"""
Python program to find the second most frequent character in a string.
"""

# using dictionary
def second_most_frequent(input_string):
    freq_dict = {}
    for char in input_string:
        freq_dict[char] = freq_dict.get(char, 0) + 1

    sorted_dict = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
    if len(sorted_dict) > 1:
        return sorted_dict[1][0]
    else:
        return None

str1 = "harsh saxena"
print(second_most_frequent(str1))


# using Counter
from collections import Counter

def second_most_frequent_1(input_string):
    counter_obj = Counter(input_string)
    counts = counter_obj.most_common()
    return counts[1][0]

print(second_most_frequent_1(str1))