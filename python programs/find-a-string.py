# You have to print the number of times that the substring occurs in the given string.
# String traversal will take place from left to right, not from right to left.

def count_substring(string, sub_string):
    count = 0
    index = 0
    while index <= len(string) - len(sub_string):
        if string[index:index+len(sub_string)] == sub_string:
            count+=1
            index+=1
        else:
            index+=1
    return count

string = input("enter the string: ")
sub_string = input("enter the sub string: ")
print("Number of occurrence:", count_substring(string, sub_string))