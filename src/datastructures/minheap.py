from unittest import TestCase
import math


class MinHeap:
    def __init__(self):
        self.heap = []

    def build_heap(self, alist):
        for val in alist:
            self.add(val)

    def add(self, val):
        self.heap.append(val)
        self._rebalance_addition(len(self.heap) - 1)

    def pop_min(self):
        new_min = self.heap.pop()
        minimum = self.heap[0]
        self.heap[0] = new_min
        self._rebalance_pop(0)
        return minimum

    def _rebalance_addition(self, n):
        if n != 0:
            parent = self._get_parent(n)
            if self.heap[parent] > self.heap[n]:
                self.heap[parent], self.heap[n] = self.heap[n], self.heap[parent]
                self._rebalance_addition(parent)

    def _rebalance_pop(self, n):
        left = self._get_left(n)
        right = self._get_right(n)
        if left and right:
            if self.heap[left] < self.heap[n] and self.heap[left] < self.heap[right]:
                self.heap[left], self.heap[n] = self.heap[n], self.heap[left]
                self._rebalance_pop(left)
            elif self.heap[right] < self.heap[n] and self.heap[right] < self.heap[left]:
                self.heap[right], self.heap[n] = self.heap[n], self.heap[right]
                self._rebalance_pop(right)
        elif left:
            if self.heap[left] < self.heap[n]:
                self.heap[left], self.heap[n] = self.heap[n], self.heap[left]

    def _get_left(self, n):
        left = n*2 + 1
        if left < len(self.heap):
            return left

    def _get_right(self, n):
        right = n*2 + 2
        if right < len(self.heap):
            return right

    def _get_parent(self, n):
        if n != 0:
            return math.floor((n-1)/2)


class MinHeapTest(TestCase):
    def test_create_heap(self):
        input_array = [1,3,5,6,7]
        heap = MinHeap()
        for num in input_array:
            heap.add(num)
        self.assertEquals(heap.heap, input_array)

    def test_build_heap(self):
        input_array = [7,6,5,3,1]
        expect_array = [1,3,6,7,5]
        heap = MinHeap()
        heap.build_heap(input_array)
        self.assertEquals(heap.heap, expect_array)


    def test_create_heap_with_rebalance(self):
        input_array = [7,6,5,3,1]
        expect_array = [1,3,6,7,5]
        heap = MinHeap()
        for num in input_array:
            heap.add(num)
        self.assertEquals(heap.heap, expect_array)
