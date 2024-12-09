"""
Given a string s consisting of words and spaces, return the length of the last word in the string.
"""

def length_of_last_word(str):
    str_list = str.split(" ")
    for i in str_list[::-1]:
        if len(i)>0:
            return len(i)



# str = "   fly me   to   the moon  "
str = "Hello World"
print(length_of_last_word(str))