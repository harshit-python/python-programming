# You are given a string .
# Your task is to find out if any char in the string contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

if __name__ == '__main__':
    string1 = input("Enter the string: ")
    print(any(char.isalnum() for char in string1))
    print(any(char.isalpha() for char in string1))
    print(any(char.isdigit() for char in string1))
    print(any(char.islower() for char in string1))
    print(any(char.isupper() for char in string1))