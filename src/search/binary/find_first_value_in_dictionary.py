"""
[a,b,c,d,e,f,g,h]
[f,g,h,a,b,c,d,e]
find the index of a


grab the first value, base the moves off that

Values need to be unique, if not make that assumption to start
   __* <= Find this value
__|  |
|    |          
     |       __|
     |     _|
     |  __|
     |_|
"""
import unittest
def bsearch(arr):
    if arr == []:
        return False

    val = arr[0]
    floor, ceil = 0, len(arr) - 1
    while floor <= ceil:
        mid = (floor + ceil) // 2
        if arr[mid] < val:
            ceil = mid - 1
        elif arr[mid] > val:
            floor = mid + 1
    return floor
            

def shiftArray(arr, numberOfShifts):
    
    for _ in range(numberOfShifts):
        val = arr.pop()
        arr.insert(0, val)
    

class TestBSearch(unittest.TestCase):
    def test_bsearch(self):
        arr = [1,2,3,4,5,6,7,8]
        shift = 2
        shiftArray(arr, shift)
        print(arr)
        self.assertEquals(bsearch(arr), 2)


