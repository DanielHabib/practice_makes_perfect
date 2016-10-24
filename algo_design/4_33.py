'''
4-33

Search an array of distinct integers to see if asubi = i
'''


def bsearch(arr):
    floor, ceil = 0, len(arr) - 1

    while floor <= ceil:
        mid_index = (floor + ceil) // 2
        if arr[mid_index] == mid_index:
            return True
        elif arr[mid_index] > mid_index:
            ceil = mid_index - 1
        else:
            floor = mid_index + 1
    return False

import unittest
class TestBsearch(unittest.TestCase):

    def test_bsearch_fails(self):
        arr = [1,2,3,4,5,6]
        self.assertFalse(bsearch(arr))

    def test_bsearch_succeeds(self):
        arr = [-10,0,2,5,7,9]
        self.assertTrue(bsearch(arr))

    def test_bsearch_succeeds_in_0(self):
        arr = [0,6,8,10,17,19]
        self.assertTrue(bsearch(arr))

    def test_bsearch_succeeds_in_last_position(self):
        arr = [-1000,-600,-80,-11,-10,5]
        self.assertTrue(bsearch(arr))
