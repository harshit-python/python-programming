# Rotate a list to the left by a given number of positions.

list1 = [1,2,3,4,5,6,7,8,9]
shift_by = 3

n = shift_by%len(list1)
new_list = list1[n:] + list1[:n]
print(new_list)