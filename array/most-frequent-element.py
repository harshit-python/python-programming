"""
Given a list of integers, find the element that appears the most frequently.
"""

def most_frequent_element(arr1):
    max_count = 0
    count_dict = {}
    most_frequent = None
    for num in arr1:
        if num not in count_dict:
            count_dict[num] = 1
        else:
            count_dict[num] += 1
        if count_dict[num] > max_count:
            max_count = count_dict[num]
            most_frequent = num

    return most_frequent

arr1 = [1,2,3,4,5,6,7,8,9,2,3,5,2,5,4,6,5,4,5,5,7,8,9]
print(most_frequent_element(arr1))

