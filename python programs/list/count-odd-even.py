# Count the number of odd and even numbers in a list.

list1 = [1,2,3,4,5,6,7,8,9,10,11]
even_list = [i for i in list1 if i%2==0]
print("number of even numbers:", len(even_list))
print("number of odd numbers:", len(list1) - len(even_list))