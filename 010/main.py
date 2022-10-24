

# https://ithelp.ithome.com.tw/articles/10268077
# https: // ithelp.ithome.com.tw/articles/10268829
# hash: 雜湊函式
# add: 新增資料
# search: 搜尋資料
# remove: 刪除資料


# 補充 LinkedList 特性：
# 由許多節點組成，每個節點包含資料欄(value)與指標欄(next)，指標欄會指向下一個資料所在的記憶體位置。
# 因此再「追加」或「刪除」資料相當方便，因為只需要更動指標的指向，
# 但在「讀取」資料就會較費時，因為必須從串列的頭開始尋找。

class Node:
    def __init__(self, key=None, data=None):
        self.value = {}
        self.value[key] = data
        self.next = None

    def __repr__(self):
        return str(self.data)


class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.next = None
        self.count = 0

    def __str__(self):
        str_list = []
        current = self.head
        while current:
            str_list.append(str(current.value))
            current = current.next
        return "[" + "->".join(str_list) + "]"

    def __repr__(self):
        return str(self)


class HashTable:
    def __init__(self, size):
        self.size = size
        self.values = [None] * size
        self.length = 0

    def hash(self, key, size):
        hashCode = 0
        for i in range(len(key)):
            hashCode += ord(key[i])
        return hashCode % size

    def add(self, key, value):
        hashIndex = self.hash(key, self.size)
        node = Node(key, value)
        if not self.values[hashIndex]:
            self.values[hashIndex] = LinkedList(node)
        else:
            current = self.values[hashIndex].head
            while current.next:
                current = current.next
            current.next = node
        self.values[hashIndex].count += 1
        self.length += 1

    def search(self, key):
        hash = self.hash(key, self.size)
        slot = self.values[hash]
        current = slot.head
        while current:
            if key in current.value:
                return current.value[key]
            current = current.next
        return 'Data not found'

    def remove(self, key):
        hash = self.hash(key, self.size)
        slot = self.values[hash]
        current = slot.head
        while current:
            if key in current.value:
                slot.head = current.next  # 這行太厲害了
                slot.count -= 1
                self.length -= 1
                return 'Data was deleted successfully'
            current = current.next

        return 'Data is not exhausting'

    def __repr__(self):
        return str(self.values)


ht = HashTable(5)
ht.add("John", "111-111-111")
ht.add("Taylor", "222-222")
ht.add("Krish", "333-333")
ht.add("Mack", "444-444")
ht.add("Den", "555-555")
ht.add("Mike", "666-666")
ht.add("Jack", "88-88-88")
ht.add("Jimmy", "99-99")
ht.add("Harry", "121-121")
ht.add("Meet", "232-232")
ht.add("Miraj", "454-454")
ht.add("Milan", "567-567")
print(ht)

print(ht.search('Den'))  # {'Den': '555-555'}
print(ht.search('Jimmy'))  # {'Jimmy': '99-99'}
print(ht.remove('Den'))  # Data was deleted successfully
print(ht.search('Den'))  # Data not found
