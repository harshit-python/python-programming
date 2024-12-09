# You are provided with a large string and a dictionary of the words.
# You have to find if the input string can be segmented into words using the dictionary or not.

def can_segment_string(dictionary1, str1):
    for i in range(1, len(str1)+1):
        substring_1 = str1[0:i]
        if substring_1 in dictionary1:
            substring_2 = str1[i:]
            if not substring_2 or substring_2 in dictionary1 or can_segment_string(dictionary1, substring_2):
                return True


dictionary1 = ["Harsh", "Saxena", "is", "the", "greatest", "coder", "of", "all", "time"]
str1 = "HarshSaxena"
print(can_segment_string(dictionary1, str1))