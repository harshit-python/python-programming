# How can you replace string space with a given character in Python?

def string_replace(str1, char1):
    result_str = ""
    for i in str1:
        if i == " ":
            i = char1
        if i == "_":
            i = " "
        result_str += i

    return result_str

str1 = input("Enter the string you want to check: ")
char1 = input("Enter the character you want to replace space with: ")

modified_string = string_replace(str1, char1)
print(modified_string)
