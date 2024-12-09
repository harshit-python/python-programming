# Split a list into chunks of a given size.

list1 = [1,2,3,4,5,6,7,8,9]
chunk_size = 4
chunked_list = [list1[i:i+chunk_size] for i in range(0, len(list1), chunk_size)]
print(chunked_list)




