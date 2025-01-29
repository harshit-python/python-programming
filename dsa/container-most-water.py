"""
Container with Most Water
"""

def maxArea(arr):
    n = len(arr)
    area = 0
    for i in range(n):
        for j in range(i+1, n):
            area = max(area, min(arr[j], arr[i]) * (j-i))
        return area


a = [3, 1, 2, 4, 5]
print(maxArea(a))