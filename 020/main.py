# https://ithelp.ithome.com.tw/articles/10280844
# Binary search

data = [10, 15, 25, 40, 45, 55, 60, 80, 90]
target = 10


def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    mid = None
    while start <= end:
        mid = int((end+start)/2)
        if target > arr[mid]:
            start = mid + 1
        elif target < arr[mid]:
            end = mid - 1
        else:
            return mid

    return None


print(binary_search(data, target))
