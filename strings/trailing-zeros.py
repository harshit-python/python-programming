# Given an integer n, return the number of trailing zeroes in n factorial n!

def factorial_trailing_zeros(n):
    fact = n
    while n > 1:
        fact *= n - 1
        n -= 1

    trailing_zeros = []
    for i in str(fact)[::-1]:
        if i == "0":
            trailing_zeros.append(i)
        else:
            break
    return len(trailing_zeros)

number1 = int(input("Enter the number to check: "))
trailing_zeros_length = factorial_trailing_zeros(number1)
print(f"Number of trailing zeros in factorial of {number1} is/are: {trailing_zeros_length}")