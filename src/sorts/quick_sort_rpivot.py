import random

def quicksort( aList ):
    _quicksort( aList, 0, len( aList ) - 1 )

def _quicksort( aList, first, last ):
    if first < last:
      pivot = partition( aList, first, last )
      _quicksort( aList, first, pivot - 1 )
      _quicksort( aList, pivot + 1, last )

def partition( aList, first, last ) :
    pivot = first + random.randrange( last - first + 1 )
    swap( aList, pivot, last )
    for i in range( first, last ):
      if aList[i] <= aList[last]:
        swap( aList, i, first )
        first += 1

    swap( aList, first, last )
    return first

def swap( A, x, y ):
  A[x],A[y]=A[y],A[x]

def qsort(alist):
    """It works!"""
    quicksort_helper(alist, 0 ,len(alist) - 1)

def quicksort_helper(alist, first, last):
    if first < last:
        pivot = _partition(alist, first, last)
        quicksort_helper(alist, first, pivot - 1)
        quicksort_helper(alist, pivot + 1, last)

def _partition(alist, first, last):
    pivot = first + random.randrange(last - first + 1)
    swap(alist, pivot, last)
    for i in range(first, last):
        if alist[i] <= alist[last]:
            swap(alist, i, first)
            first += 1
    swap(alist, first, last)
    return first

if __name__ == '__main__':
    alist = [3,2,4,15,6,7,2,3,5,7,2,3,2,6]
    qsort(alist)
    print(alist)