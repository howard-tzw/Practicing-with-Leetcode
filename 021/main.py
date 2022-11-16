# https://ithelp.ithome.com.tw/articles/10281248

# Interpolation Search
# 看不懂

data = [10, 20, 30, 40, 50, 60, 70, 80, 90]
target = 40


def interpolation_search(arr, target):
    start = 0
    end = len(arr)-1

    while start <= end:
        mid = (target - arr[start]) * \
            (end - start) // (arr[end] - arr[start]) + start

        if target == arr[mid]:
            return "有搜尋結果：在第" + str(mid+1) + "項"
        else:
            if target < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return "無搜尋結果"


print(interpolation_search(data, target))
