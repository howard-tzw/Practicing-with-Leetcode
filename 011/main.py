# https://ithelp.ithome.com.tw/articles/10277847
# Shell Sort

# 暫時無法理解這套演算法的奧妙...

data = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]


def shell_sort(data):
    n = len(data)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            tmp = data[i]
            j = i
            while j >= gap and data[j-gap] > tmp:
                data[j] = data[j-gap]
                j = j-gap
            data[j] = tmp
        gap = gap // 2
    return data


print(shell_sort(data))
