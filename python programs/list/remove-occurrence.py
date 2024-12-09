# Remove all occurrences of a specific element from the list.

list1 = [1,2,3,3,4,5,5,6]
target_num = 2

new_list = [num for num in list1 if num!=target_num]
print(new_list)