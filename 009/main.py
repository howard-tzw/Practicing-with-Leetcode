# https://ithelp.ithome.com.tw/articles/10277360
# Insertion sort

# (n-1) + (n-2) + .... + 1 = n(n-1) / 2
# 平均時間複雜度為: O(n²)

# 這裡使用了如何在陣列中移動一個值的寫法

data = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]


# 覆蓋 key 的位置，然後一個一個後移，最後再填入 key
def insertion_sort(data):
    n = len(data)
    for i in range(n-1):
        key = data[i+1]
        j = i
        while j >= 0 and key < data[j]:
            data[j+1] = data[j]
            j -= 1
        data[j+1] = key

    return data


# 如果比較小，就跟前一個互換位置
def insertion_sort2(data):
    for i in range(len(data)-1):
        target = i+1
        j = i
        while j >= 0:
            if data[target] < data[j]:
                data[target], data[j] = data[j], data[target]
                target = j
            j -= 1
    return data


print(insertion_sort2(data))
