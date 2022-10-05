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

    def insertAt(self, index, data):
        if index < 0 or index >= self.size():
            return
        node = Node(data)
        previous = None
        count = 0
        current = self.head
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            while index != count:
                previous = current
                current = current.next
                count += 1
            new_node = Node(data, previous.next)
            previous.next = new_node

    def removeAt(self, index):
        if index < 0 or index >= self.size():
            return

        count = 0
        current = self.head
        previous = None
        if index == 0:
            self.head = self.head.next
        else:
            while index != count:
                previous = current
                current = current.next
                count += 1
            previous.next = current.next

    def remove(self, data):
        node = self.head
        previous = None
        if self.head.data == data:
            self.head = self.head.next
        else:
            while node:
                previous = node
                node = node.next
                if node.data == data:
                    previous.next = node.next
                    return

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
ll.append('dd')
print('indexOf dd: ', ll.indexOf('dd'))
print('size: ', ll.size())

print(ll.print())
ll.insertAt(1, 'hello')
print(ll.print())

ll.removeAt(3)
print(ll.print())

ll.remove('hello')
print(ll.print())

print('============== quicksort ================')

# O(n log n)
data = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]
# def quicksort(data):
