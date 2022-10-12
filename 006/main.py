# Linked Stack

class StackNode():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedStack():
    def __init__(self, top=None):
        self.top = top

    def push(self, data):
        if self.top is None:
            self.top = StackNode(data)
        else:
            node = StackNode(data, self.top)
            self.top = node

    def pop(self):
        if self.top is None:
            return None
        else:
            self.top = self.top.next

    def peek(self):
        if self.top is None:
            return None
        return self.top.data

    def size(self):
        count = 0
        node = self.top
        while node:
            node = node.next
            count += 1
        return count


stack = LinkedStack()
stack.push('20')
stack.push('30')
stack.push('40')
print(stack.size())  # 3
print(stack.peek())  # "40"
stack.pop()
print(stack.peek())  # "30"
print(stack.size())  # 2
stack.pop()
print(stack.size())  # 1
print(stack.peek())  # "20"
