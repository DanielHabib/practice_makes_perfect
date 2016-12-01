"""
Find number of instances of a specific integer in a sorted array


[1,2,3,4,4,4,5,6,7,8]

"""

from unittest import TestCase

def bsearch(arr, num):
    floor, ceil = 0, len(arr) - 1
    # Left Bound
    while floor <= ceil:
        midIndex = (floor + ceil) // 2
        midValue = arr[midIndex]
        if midValue < num:
            floor = midIndex + 1
        else: # midValue >= num
            ceil = midIndex - 1
    leftIndex = floor

    # Right Bound
    floor, ceil = 0, len(arr) - 1
    while floor <= ceil:
        midIndex = (floor + ceil) // 2
        midValue = arr[midIndex]
        if midValue <= num:
            floor = midIndex + 1
        else: # midValue > num
            ceil = midIndex - 1
    rightIndex = ceil
    
    return rightIndex - leftIndex + 1 # Handles -1 case subtely



class BSearchTest(TestCase):
    def test_bsearch_odd(self):
        num = 5
        result = 7
        arr = [1,2,3,4,5,5,5,5,5,5,5,6,7,8,9,10]
        self.assertEquals(result, bsearch(arr,num))

    def test_bsearch_even(self):
        num = 5
        result = 6
        arr = [1,2,3,4,5,5,5,5,5,5,6,7,8,9,10]
        self.assertEquals(result, bsearch(arr,num))

    def test_bsearch_no_match(self):
        num = 5
        result = 0
        arr = [1,2,3,4,6,7,8,9,10]
        self.assertEquals(result, bsearch(arr,num))

    def test_bsearch_all_match(self):
        num = 5
        arr = [5,5,5,5,5,5,5,5,5,5,5,5]
        result = len(arr)
        self.assertEquals(result, bsearch(arr,num))
