# https://ithelp.ithome.com.tw/articles/10267386
# LinkedQueue
# enqueue: 尾端新增元素
# dequeue: 從前端移除元素
# peek: 查看最前端元素
# size: 此佇列的元素量

class QueueNode():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedQueue():
    def __init__(self) -> None:
        self.front = None
        self.rear = None

    def enqueue(self, data):
        if self.front is None:
            self.front = QueueNode(data)
            self.rear = self.front
        else:
            self.rear.next = QueueNode(data)
            self.rear = self.rear.next

    def dequeue(self):
        if self.front is None:
            return None
        if self.front == self.rear:
            self.rear = None
        self.front = self.front.next

    def size(self):
        node = self.front
        count = 0
        while node:
            node = node.next
            count += 1
        return count

    def peek(self):
        if self.front is None:
            return None
        return self.front.data


queue = LinkedQueue()
queue.enqueue('20')
queue.enqueue('30')
queue.enqueue('40')
print(queue.peek())  # 20
print(queue.size())  # 3
queue.dequeue()
print(queue.peek())  # 30
print(queue.size())  # 2
queue.dequeue()
print(queue.peek())  # 40
print(queue.size())  # 1
queue.dequeue()
print(queue.peek())  # None
print(queue.size())  # 0
