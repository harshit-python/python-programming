# Check if all elements in the list are positive.

list1 = [1,2,3,4,5,6]
list2 = [1,-2,3,4,-5,6]

print(all(num>0 for num in list1))
print(all(num>0 for num in list2))
