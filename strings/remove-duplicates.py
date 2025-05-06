"""
Python program to remove duplicates from a given string
"""

def remove_duplicates(input_string):
    seen = set()
    result_string = ""
    for s in input_string:
        if s not in seen:
            seen.add(s)
            result_string += s

    return result_string

str1 = "harsh saxena"
print(remove_duplicates(str1))