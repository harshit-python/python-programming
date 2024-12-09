# Flatten a list of lists into a single list.

list1 = [[1,2,3,4], [4,5,6,7], [2,3,4,5,6]]
flattened_list = [item for sub_list in list1 for item in sub_list]
print(flattened_list)