'''
Assumumptions: Unique Values, All values are integers, Shift can = 0
Axium: Sorted prior to shift



Qs:
    why return arr[ceil]. How to choose which index to return


SIMPLEST ARRAY ANALYSIS: Confirms what my `UNKNOWN_CONDITIONAL` should be
    tells me which pointer to return
    It Describes which direction we should shift over
'''

def bsearch(arr): # Augmented Binary Search

    if len(arr) == 0: return None
    if len(arr) == 1: return arr[0]

    first = arr[0]
    floor, ceil = 0, len(arr) - 1

    while floor <= ceil: # Questionable Conditional
        mid = (floor + ceil) // 2
        if arr[mid] < first:
            ceil = mid - 1
        elif arr[mid] > first:
            floor = mid + 1
        else:
            pass
    return arr[ceil]


import unittest

class TestAugmentedBsearch(unittest.TestCase):

    def test_bsearch(self):
        arr = [9,10,1,2,3,4,5,6,7]
        maxVal = max(arr)
        self.assertEquals(maxVal, bsearch(arr))

    def test_bsearch_unshifted(self):
        arr = [1,2,3,4,5,6,7]
        maxVal = max(arr)
        self.assertEquals(maxVal, bsearch(arr))
