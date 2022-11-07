# https://ithelp.ithome.com.tw/articles/10279239
# Heap Sort

def maxHeapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    # 若左子樹大於根節點時
    if l < n and arr[i] < arr[l]:
        largest = l

    # 若右子樹大於跟節點時
    if r < n and arr[r] > arr[largest]:
        largest = r

    # 根節點不是最大時
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        maxHeapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # 建立最大堆積
    for i in range(n // 2 - 1, -1, -1):
        maxHeapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        maxHeapify(arr, i, 0)


data = [30, 20, 15, 1, 10, 5]
heap_sort(data)
print(data)

for i in range(3, -1, -1):
    print(i)
