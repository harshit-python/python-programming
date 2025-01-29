# Calculate the product of all elements in the list.

from functools import reduce
import operator

list1 = [1,2,3,4,5]
final_list = reduce(operator.mul, list1, 1)
print(final_list)