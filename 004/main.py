
# O(n log n)
arr = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]
# def quicksort(data):

# 遞迴版
# 容易理解，但會影響到空間複雜度，每次都需要申請兩個子數列的記憶體空間，遞迴的深度越多，需要記憶體空間就越大。


def quicksort_1(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = []
    right = []
    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    return quicksort_1(left) + [pivot] + quicksort_1(right)


sorted = quicksort_1(arr)
print(sorted)

# 原地交換版 In-Place (Lomuto partition scheme)
