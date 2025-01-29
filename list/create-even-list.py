# Create a new list containing only the even numbers from the original list.

list1 = [1,2,3,4,5,6,7,8,9,10]
even_list = [item for item in list1 if item%2 == 0]
print(even_list)