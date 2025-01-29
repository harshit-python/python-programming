# Find the missing number in the array

def find_missing_number(array1):
    array_sum = sum(array1)

    n = len(array1) + 1             # since there is exactly one number missing
    total_sum = (n*(n+1))/2
    missing_number = total_sum - array_sum
    return int(missing_number)

array1 = [1,5,6,3,4]
missing_number = find_missing_number(array1)
print("Missing number from the array is:", missing_number)