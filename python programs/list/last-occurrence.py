# Find the index of the last occurrence of an element in a list.

list1 = [1,2,3,4,5,6,7,8,9,6,7,4,2,3,1]
target = 3

last_occurrence = len(list1) - 1 - list1[::-1].index(2)
print(last_occurrence)