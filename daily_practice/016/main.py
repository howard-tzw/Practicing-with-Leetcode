# https://ithelp.ithome.com.tw/articles/10273685
# Heap

import heapq


class MaxHeap:
    def __init__(self):
        self.maxheap = []

    def push(self, key):
        heapq.heappush(self.maxheap, key)
        heapq._heapify_max(self.maxheap)

    def getRoot(self):
        return self.maxheap[0]

    def popRoot(self):
        heapq.heappop(self.maxheap)
        heapq._heapify_max(self.maxheap)

    def printHeap(self):
        print(self.maxheap)


heap = MaxHeap()
heap.push(20)
heap.push(10)
heap.push(5)
heap.push(80)
heap.push(75)
heap.push(78)
heap.push(72)
heap.push(73)
heap.printHeap()  # 80, 75, 78, 73, 20, 5, 72, 10
heap.popRoot()
heap.printHeap()  # 78, 75, 72, 73, 20, 5, 10
heap.popRoot()
heap.printHeap()  # 75, 73, 10, 72, 20, 5
