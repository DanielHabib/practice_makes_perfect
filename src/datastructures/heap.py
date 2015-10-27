from unittest import TestCase
import math
"""Max Heap Implemented by an array y'all"""
class MaxHeap:
    def __init__(self):
        self.heap = []

    def add_node(self, val):
       self.heap.append(val)
       length = len(self.heap)
       self._addition_rebalance(length-1)

    def _addition_rebalance(self, n):
        """Rebalance Through addition ,,,, Look up"""
        if n != 0:
            parent = self._find_parent(n)
            if self.heap[n] > self.heap[parent]:
                self.heap[n], self.heap[parent] = self.heap[parent], self.heap[n]
                self._addition_rebalance(parent)

    def get_max(self):
        maximium_val = self.heap[0]
        print(self.heap)
        if not self.heap:
            return None
        if len(self.heap) == 1:
            val = self.heap.pop()
            return val
        self.heap[0] = self.heap.pop()
        self._rebalance_delete(0)
        return maximium_val

    def _rebalance_delete(self, n):
        left = self._find_left(n)
        right = self._find_right(n)
        if left and right:
            if self.heap[left] > self.heap[n] and self.heap[left] > self.heap[right]:
                self.heap[left], self.heap[n] = self.heap[n], self.heap[left]
                self._rebalance_delete(left)
            elif self.heap[right] > self.heap[n] and self.heap[right] > self.heap[left]:
                self.heap[right], self.heap[n] = self.heap[n], self.heap[right]
                self._rebalance_delete(right)
        elif left:
            if self.heap[left] > self.heap[n]:
                self.heap[left], self.heap[n] = self.heap[n], self.heap[left]

    def _find_parent(self, n):
        return math.floor((n-1)/2)

    def _find_left(self, n):
        left = n*2 + 1
        if left < len(self.heap):
            return left

    def _find_right(self, n):
        right = n*2 + 2
        if right < len(self.heap):
            return right

class MaxHeapTest(TestCase):
    def test_create_heap(self):
        input_array = [1,3,5,6,7]
        expect_array = [7,6,3,1,5]
        heap = MaxHeap()
        for num in input_array:
            heap.add_node(num)
        self.assertEquals(heap.heap, expect_array)

    def test_get_max_from_heap(self):
        input_array = [1,3,5,6,7]
        heap = MaxHeap()
        for num in input_array:
            heap.add_node(num)
        self.assertEquals(7, heap.get_max())
        self.assertEquals(6, heap.get_max())
        self.assertEquals(5, heap.get_max())
        self.assertEquals(3, heap.get_max())
        self.assertEquals(1, heap.get_max())






