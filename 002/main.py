

data = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]

# https://ithelp.ithome.com.tw/articles/10202160
# O(n^2)


def bubblesort(data):
    for i in range(len(data)-2):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]


bubblesort(data)
print(data)
