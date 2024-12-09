"""
Given an input string s, reverse the order of the words.
"""

def reverse_words_of_string(string):
    str_list = string.split()
    reverse_list = str_list[::-1]
    reverse_string = " ".join(reverse_list)
    return reverse_string



# string = "the sky is blue"
# string = "  hello world  "
string = "example   good a"
print(reverse_words_of_string(string))