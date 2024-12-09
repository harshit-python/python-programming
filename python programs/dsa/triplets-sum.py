"""
Given an array arr[], the task is to find all possible indices {i, j, k} of triplet {arr[i], arr[j], arr[k]}
such that their sum is equal to zero and all indices in a triplet should be distinct (i != j, j != k, k != i).
We need to return indices of a triplet in sorted order, i.e., i < j < k.
"""

def findTriplets(arr):
    n = len(arr)
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == 0:
                    return arr[i], arr[j], arr[k]


arr = [0, -1, 2, -3, 1]
res = findTriplets(arr)
print(res)
