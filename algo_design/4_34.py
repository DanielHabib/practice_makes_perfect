'''
4-34

Search a sorted distinct integer array containing values 1-m but missing a few
find the smallest missing value

'''


def bsearch(arr):
    if arr[0] != 1:
        return 1

    floor, ceil = 0, len(arr) - 1
    while floor <= ceil:
        mid = (floor + ceil) // 2
        if mid - floor < arr[mid] - arr[floor]:
            ceil = mid - 1
        elif ceil - mid < arr[ceil] - arr[mid]:
            floor = mid + 1
        else:
            ceil = ceil - 1

    return arr[ceil] + 1

import unittest
class TestBsearch(unittest.TestCase):

    def test_bsearch(self):
        arr = [1,3,4,5,6]
        self.assertEquals(2,bsearch(arr))

    def test_bsearch_succeeds(self):
        arr = [1,2,3,4,5,9]
        self.assertEquals(6,bsearch(arr))

    def test_bsearch_with_two_separated_missing_values(self):
        arr = [1,3,4,5,9]
        self.assertEquals(2,bsearch(arr))

    def test_succeeds_when_trailing_is_missing(self):
        arr = [1,2,3,4,5,6,7,8]
        self.assertEquals(9, bsearch(arr))
