"""
Merge K sorted lists | Trick is to use a heap to hit O(nlogk) as opposed to naive O(nk) solution
"""
import heapq
import unittest

class Node:
    def __init__(self, value, listIndex):
        self.__dict__.update({x: k for x,k in locals().items() if x != 'self'})
    def __lt__(self, other):
        return self.value < other.value


def mergeLists(lists):
    heap, sortedList = [], []
    for index, a_list in enumerate(lists):
        if a_list != []:
            heapq.heappush(heap, Node(a_list.pop(0), index))
    while len(heap) != 0:
        node = heapq.heappop(heap)
        sortedList.append(node.value)
        if lists[node.listIndex] != []:
            node = Node(lists[node.listIndex].pop(0), node.listIndex)
            heapq.heappush(heap, node)

    return sortedList


class TestMergeLists(unittest.TestCase):
    def test_merge_lists(self):
        lists = [
            [4,8],
            [6,9],
            [2,7]
        ]
        self.assertEquals(mergeLists(lists), [2,4,6,7,8,9])
