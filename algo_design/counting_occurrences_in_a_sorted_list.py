'''
Find how many times value k appears in a sorted list


Approach:
    Use Binary Search to look for the boundaries of the chunk of k not the value
    k itself.
    ex:
        a = [1,2,2,2,3], k = 2 => 3 = high - low + 1 = 3 - 1 + 1
    Leverage Binary Search Twice
'''

def bsearch(arr, value):

    low, high = 0, len(arr) - 1
    while low <= high: # Find the upper bounds
        mid = (high + low) // 2
        if value < arr[mid]:
            high = mid - 1
        elif value > arr[mid]:
            low = mid + 1
        elif value == arr[mid]:
            low = mid + 1
    top = high
    print high
    print low

    low = 0

    while low <= high:
        mid = (high + low) // 2
        if value < arr[mid]:
            high = mid - 1
        elif value > arr[mid]:
            low = mid + 1
        elif value == arr[mid]:
            high = mid - 1

    print top
    print low

    return top - low + 1

import unittest
class TestBSearch(unittest.TestCase):

    def test_bsearch(self):
        value = 2
        answer = 2
        arr = [1,2,2,3]
        self.assertEquals(answer, bsearch(arr, value))

    def test_bsearch_empty(self):
        self.assertEquals(0, bsearch([], 1))
