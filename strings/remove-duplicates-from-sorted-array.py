# Remove duplicates from sorted array

def remove_duplicates(array1):
    if not array1:
        return 0

    inserting_index = 1
    for i in range(1, len(array1)):
        if array1[i-1] != array1[i]:
            array1[inserting_index] = array1[i]
            inserting_index += 1

    return array1

array1 = [1,1,2,2,2,3,3,4,4,4,5,5]
result_array = remove_duplicates(array1)
print(result_array)
