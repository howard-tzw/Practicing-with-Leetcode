# https://ithelp.ithome.com.tw/articles/10278179

# 分割：分割含有 n 個資料需要 n-1 次，O(n)。
# 合併：合併的兩邊共用 n 個元素，每次都是比較最左邊的資料，將較小的加到新陣列中，因此每次排序與合併必須經過 n 次，每回合log n次，O(log n)。
# 平均時間複雜度為: O(n log n)

data = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]


def merge(left, right):    # 合併
    result = []
    while len(left) and len(right):
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    result = result+left if len(left) else result+right
    return result


def merge_sort(arr):    # 分割
    if len(arr) < 2:
        return arr

    mid = len(arr)//2
    leftArray = arr[:mid]
    rightArray = arr[mid:]

    return merge(merge_sort(leftArray), merge_sort(rightArray))


print(merge_sort(data))
