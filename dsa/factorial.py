# find factorial of large number

def factorial(num):
    fact = 1
    for i in range(2, num+1):
        fact *= i
    return fact


num = int(input("Enter the number: " ))
response = factorial(num)
print(response)