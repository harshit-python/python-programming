"""
Find the missing number in an array containing n distinct numbers from 0 to n.
"""

def missing_number(arr1):
    n = len(arr1)
    expected_sum = (n*(n+1))/2
    actual_sum = sum(arr1)
    missing_num = actual_sum - expected_sum
    return missing_num

arr1 = [1,2,4,5,6]
print(missing_number(arr1))