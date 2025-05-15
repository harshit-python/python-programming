"""
Given an array of integers, find all duplicates in the array.
"""

def find_duplicates(arr1):
    count_dict = {}
    duplicate_list = []
    for num in arr1:
        count_dict[num] = count_dict.get(num, 0) + 1
    for key, value in count_dict.items():
        if value > 1:
            duplicate_list.append(key)

    return duplicate_list

arr1 = [4, 3, 2, 7, 8, 2, 3, 1]
print(find_duplicates(arr1))