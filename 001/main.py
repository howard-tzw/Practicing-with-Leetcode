import enum
import numpy as np

a = np.array([1, 2, 3])


# NumPy 是 Python 的一個套件，大部分人會使用它來運用 Array 資料型態，與內建的 List 相比，
# List在記憶體中儲存的方式有很大的差異。List 的每個資料可以是不同的資料型別，
# 因此這些資料在記憶體中的儲存位置是很難以預測的。而 Array 規定每一個資料都必須有相同的資料型別，
# 它們在記憶體上的儲存位置會完全排在一起，因此 Array 的存取速度會比 List 快。

# bucket sort
# 1. 建立桶子
# 2. 分類
# 3. 讀取
data = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]


def bucketsort(data):
    max_score = 100
    bucket = []

    for i in range(max_score+1):
        bucket.append(0)

    for score in data:
        bucket[score] = bucket[score]+1

    index = 0
    for i in range(len(bucket)):
        if (bucket[i] != 0):
            for j in range(bucket[i]):
                data[index] = i
                index += 1


bucketsort(data)


data2 = [['Abby', 58], ['Julia', 44], ['Jane', 31], ['Stephen', 76], ['Ryn', 82], [
    'Justin', 99], ['Caroline', 65], ['James', 87], ['Damon', 25], ['Elena', 76]]

# 文章解法，覺得有問題


def bucketsort2(data):
    max_score = 100
    bucket = []
    def bucket_num(x): return int(x/33)

    for i in range(max_score+1):
        bucket.append([])

    for x in data2:
        index = bucket_num(x[1])
        bucket[index].append(x)

    for i, flag in enumerate(bucket):
        if flag != []:
            bucket[i] = sorted(bucket[i], key=lambda x: x[1])

    index = 0
    for i in bucket:
        if i != []:
            for j in i:
                data[index] = j
                index += 1

# bucketsort2(data2)


# 內建函式解
sorted(data2, key=lambda x: x[1])

# Linked List
# https://ithelp.ithome.com.tw/articles/10264368


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)

        # insertAt
        # removeAt
        # remove

    def indexOf(self, data):
        node = self.head
        index = 0
        while node:
            if (node.data == data):
                return index
            node = node.next
            index += 1
        return None

    def size(self):
        node = self.head
        count = 0
        while node:
            node = node.next
            count += 1
        return count

    def isEmpty(self):
        return self.head == None

    def print(self):
        if not self.head:
            print(None)
            return
        cur = self.head
        while cur:
            print(cur.data, end=' -> ')
            cur = cur.next


ll = LinkedList()
ll.append('abc')
ll.append('cde')
print(ll.print())
ll.append('dd')
print('indexOf dd: ', ll.indexOf('dd'))
print('size: ', ll.size())
