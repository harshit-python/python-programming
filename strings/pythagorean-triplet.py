# Find Pythagorean Triplet in an array

def check_triplet(array1):
    n = len(array1)
    for i in range(n):
        array1[i] = array1[i]**2
    array1 = sorted(array1)

    for i in range(n-1, 1, -1):
        set1 = set()
        for j in range(i-1, -1, -1):
            if array1[i] - array1[j] in set1:
                return True
            set1.add(array1[j])


array1 = [1,2,3,4,5,6]
result = check_triplet(array1)
print(result)
