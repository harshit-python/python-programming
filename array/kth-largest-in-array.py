"""
Find the kth largest element in an unsorted array.
It is the kth largest element in sorted order, not the kth distinct element.
"""
import heapq


def find_kth_largest(arr1, k):
    heap = arr1[:k]
    heapq.heapify(heap)
    for num in arr1[k:]:
        if num > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, num)
    return heap[0]



arr1 = [3, 2, 1, 5, 6, 7, 8, 4]
k = 2
print(find_kth_largest(arr1, k))