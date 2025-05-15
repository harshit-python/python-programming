"""
Given an array nums,
write a function to move all 0s to the end of it while maintaining the relative order of the non-zero elements.
"""

def move_zeroes(arr1):
    zero_index = 0
    for i in range(len(arr1)):
        if arr1[i] != 0:
            arr1[zero_index] = arr1[i]
            zero_index += 1

    for i in range(zero_index, len(arr1)):
        arr1[i] = 0

    return arr1

arr1 = [0, 1, 0, 3, 12]
print(move_zeroes(arr1))