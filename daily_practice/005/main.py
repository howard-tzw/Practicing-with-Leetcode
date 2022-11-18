# key word: divide and conquer, 分割交換排序法


arr = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]


# 原地交換版本(In-Place)-Lomuto partition scheme

def quicksort(arr, start, end):
    if start < end:
        pivotIndex = partition(arr, start, end)
        quicksort(arr, start, pivotIndex-1)
        quicksort(arr, pivotIndex+1, end)
    return arr


def partition(arr, start, end):
    nextIndex = start  # 指標：紀錄下一個小於 pivot 的元素要交換到的位置
    pivot = arr[end]  # 基準值
    for i in range(start, len(arr)-1):
        if arr[i] < pivot:  # 小於 pivot 的索引
            arr[i], arr[nextIndex] = arr[nextIndex], arr[i]  # 交換
            nextIndex += 1  # 交換後指標往下一位置移動
    arr[nextIndex], arr[end] = arr[end], arr[nextIndex]  # 最後將 pivot 與指標交換
    return nextIndex


print(quicksort(arr, 0, len(arr)-1))

# 原地交換版本(In-Place)-Hoare partition scheme
# 尚未把邏輯細節釐清

arr2 = [30, 10, 40, 5, 70, 15, 60, 20, 50, 25]


def quicksort_2(arr, start, end):
    if start < end:
        pivotIndex = partition_2(arr, start, end)
        quicksort_2(arr, start, pivotIndex-1)
        quicksort_2(arr, pivotIndex+1, end)
    return arr


def partition_2(arr, start, end):
    pivot = arr[start]
    leftPointer = start+1
    rightPointer = end
    done = False
    while not done:
        while arr[leftPointer] <= pivot and leftPointer <= rightPointer:
            leftPointer += 1
        while arr[rightPointer] >= pivot and rightPointer >= leftPointer:
            rightPointer -= 1

        if leftPointer > rightPointer:
            done = True
        else:
            arr[leftPointer], arr[rightPointer] = arr[rightPointer], arr[leftPointer]

    arr[start], arr[rightPointer] = arr[rightPointer], arr[start]
    return rightPointer


print(quicksort_2(arr2, 0, len(arr2)-1))
