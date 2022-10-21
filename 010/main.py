

# https://ithelp.ithome.com.tw/articles/10268077
# https: // ithelp.ithome.com.tw/articles/10268829
# hash: 雜湊函式
# add: 新增資料
# search: 搜尋資料
# remove: 刪除資料

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

# class HashTable:
