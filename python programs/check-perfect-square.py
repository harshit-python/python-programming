# Given a positive integer num, write a function that returns True if num is a perfect square else False.

def validate_square(num1):
    square_root = num1**0.5
    square = square_root**2
    if square == num1:
        return True
    else:
        return False

num1 = int(input("Enter a number to check if it's a perfect square: "))
check = validate_square(num1)
if check:
    print(f"{num1} is a perfect square")
else:
    print(f"{num1} is not a perfect square")