"""
Given a sorted array, remove the duplicates so each element appears only once.
Return the length of the modified array and modify the input array
to contain unique elements in the first `k` positions, where `k` is the length of the unique elements.
"""


def remove_duplicates(arr1):
    i = 0
    for j in range(1, len(arr1)):
        if arr1[i] != arr1[j]:
            i += 1
            arr1[i] = arr1[j]
    print(arr1)
    return i+1


arr1 = [0, 0, 1, 1, 1, 2, 2, 3, 4]
print(remove_duplicates(arr1))


# if we want sub-array

def remove_duplicates1(arr1):
    i = 0
    for j in range(1, len(arr1)):
        if arr1[i] != arr1[j]:
            i += 1
            arr1[i] = arr1[j]
    return arr1[:i+1]


arr1 = [0, 0, 1, 1, 1, 2, 2, 3, 4]
print(remove_duplicates1(arr1))
