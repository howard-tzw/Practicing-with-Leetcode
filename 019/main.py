# https://ithelp.ithome.com.tw/articles/10279960
# Radix Sort

def radix_sort(arr):
    maxNum = max(arr)
    digits = 1
    while maxNum >= 10**digits:
        digits += 1
    for i in range(digits):
        # 產生空桶子
        buckets = [[] for _ in range(10)]

        # 依據位數大小分類
        for j in arr:
            radix = int(j/10**i % 10)
            buckets[radix].append(j)

        # 合併桶子的資料
        x = 0
        for y in range(10):
            for num in buckets[y]:
                arr[x] = num
                x += 1

    return arr


data = [28, 96, 5, 33, 60, 169, 170, 249, 362, 44, 84, 123]

print(radix_sort(data))
