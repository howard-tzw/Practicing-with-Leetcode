# https://ithelp.ithome.com.tw/articles/10272982
# binary search tree

# insert: 新增元素進入樹中
# delete: 從樹中刪除此元素
# preOrderTraversal: 前序走訪
# inOrderTraversal: 中序走訪
# postOrderTraversal: 後序走訪
# search: 搜尋此元素是否在樹中

class BinarySearchTree:
    def __init__(self, data=None):
        self.data = data
        self.right = None
        self.left = None

    def insert(self, data):
        if not self.data:
            self.data = data
            return
        if self.data == data:
            return
        if data < self.data:
            if self.left:
                self.left.insert(data)
                return
            self.left = BinarySearchTree(data)
            return
        if self.right:
            self.right.insert(data)
            return
        self.right = BinarySearchTree(data)

    # 看不懂
    def delete(self, data):
        if self == None:
            return self
        if data < self.data:
            if self.left:
                self.left = self.left.delete(data)
            return self
        if data > self.data:
            if self.right:
                self.right = self.right.delete(data)
                return self
        if self.right == None:
            return self.left
        if self.left == None:
            return self.right
        aux = self.right
        while aux.left:
            aux = aux.left
        self.data = aux.data
        self.right = self.right.delete(aux.data)
        return self

    def preOrderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.preOrderTraversal(root.left)
            res = res + self.preOrderTraversal(root.right)
        return res

    def inOrderTraversal(self, root):
        res = []
        if root:
            res = self.inOrderTraversal(root.left)
            res.append(root.data)
            res = res + self.inOrderTraversal(root.right)
        return res

    def postOrderTraversal(self, root):
        res = []
        if root:
            res = self.postOrderTraversal(root.left)
            res = res + self.postOrderTraversal(root.right)
            res.append(root.data)
        return res

    def search(self, data):
        if not self.data:
            return False
        if data < self.data:
            if self.left == None:
                return False
            return self.left.search(data)

        if data > self.data:
            if self.right == None:
                return False
            return self.right.search(data)

        if data == self.data:
            return True


tree = BinarySearchTree()
tree.insert(11)
tree.insert(7)
tree.insert(15)
tree.insert(5)
tree.insert(3)
tree.insert(9)
print(tree.preOrderTraversal(tree))  # 11, 7, 5, 3, 9, 15
print(tree.inOrderTraversal(tree))  # 3, 5, 7, 9, 11, 15
print(tree.postOrderTraversal(tree))  # 3, 5, 9, 7, 15, 11
print(tree.search(9))  # True
tree.delete(9)
print(tree.search(9))  # False
