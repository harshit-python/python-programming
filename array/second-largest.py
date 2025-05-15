"""
find the second-largest element in an array without sorting, and while treating duplicates as separate values
"""


def second_largest(arr1):
    first, second = float('-inf'), float('-inf')
    for num in arr1:
        if num > first:
            second = first
            first = num
        if num > second and num != first:
            second = num

    return second if second != float('-inf') else None

arr1 = [10, 20, 4, 45, 99, 99]
print(second_largest(arr1))