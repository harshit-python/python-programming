#  Read a given string, change the character at a given index and then print the modified string.

def mutate_string(string, position, character):
    str1 = list(string)
    str1[position] = character
    return "".join(str1)

string = input("enter your string: ")
position = int(input("enter the position in string that you want to replace: "))
character = input("enter the character by which you want to replace: ")
print("Mutated string is -", mutate_string(string, position, character))