import random

class Qsort:
    def quicksort(self, a):
        """ """
        self.split(a, 0, len(a) - 1)
    def split(self, arr, low, high):
        if high - low > 0:
            pivot = self.partition(
                    arr,
                    low,
                    high)
            self.split(arr, low, pivot - 1)
            self.split(arr, pivot + 1, high)
                    

    @staticmethod
    def chooseRandomPivot(a, b):
        return random.randint(a, b)
    
    def swap(self, arr, low, high):
        arr[low], arr[high] = arr[high], arr[low]

    def partition(self, alist, first, last):
        self.swap(alist, first, self.chooseRandomPivot(first, last))
        leftmark = first + 1
        rightmark = last

        pivotvalue = alist[first]
        while True:
            while leftmark <= rightmark and alist[leftmark] < pivotvalue:
                leftmark = leftmark + 1
            while leftmark <= rightmark and alist[rightmark] >= pivotvalue:
                rightmark = rightmark -1
            if rightmark < leftmark:
                break
            self.swap(alist, leftmark, rightmark)

        self.swap(alist, first, rightmark)
        return rightmark

from random import randint
if __name__ == '__main__':
    qsort = Qsort()
    arr = [randint(0, 100) for x  in range(6)]
    print(arr)
    qsort.quicksort(arr)
    print(arr)

    print ("Two")

    arr = [randint(0, 100) for x  in range(6)]
    arr[:2] = [55, 55]
    qsort.quicksort(arr)
    print(arr)
