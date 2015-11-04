
"""Priority Queue"""
from datastructures.minheap import MinHeap
from math import floor


class PQNode:
    def __init__(self, priority, value):
        self.priority = priority
        self.val = value


class PriorityQueue(MinHeap):

    def __init__(self):
        super().__init__()

    def add(self, priority, val):
        node = PQNode(priority, val)

        self.heap.append(node)
        self.rebalance_addition(len(self.heap) - 1)

    def rebalance_addition(self, n):
        parent = self._parent(n)
        if parent:
            if self.heap[parent].priority < self.heap[n].priority:
                self.heap[parent], self.heap[n] = self.heap[n], self.heap[parent]
                self.rebalance_addition(parent)

    def pop(self, priority, val):
        if self.heap:
            min_ = self.heap[0].value
            final = self.heap.pop()
            self.heap[0] = final
            self.rebalance_deletion(self, 0)
            return min_

    def rebalance_deletion(self, n):
        left = self._left(n)
        right = self._right(n)
        if left and right:
            if self.heap[left].priority < self.heap[n].priority and \
                        self.heap[left].priority < self.heap[right].priority:
                """Swap Left"""
                self.heap[left], self.heap[n] = self.heap[n], self.heap[left]
                self.rebalance_deletion(left)
            if self.heap[right].priority < self.heap[n].priority and \
                    self.heap[right].priority < self.heap[left].priority:
                self.heap[right], self.heap[n] = self.heap[n], self.heap[right]
                self.rebalance_deletion(right)
        if left:
            if self.heap[left].priority < self.heap[n].priority:
                self.heap[left], self.heap[n] = self.heap[n], self.heap[left]


    def _parent(n):
        if n > 0:
            return floor((n - 1) / 2)

    def _left(n):
        left = (n * 2) + 1
        if left < len(self.heap):
            return left

    def _right(n):
        right = (n * 2) + 2
        if right < len(self.heap):
            return right
