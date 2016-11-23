"""
Heap Sort

"""
import heapq
def heapsort(arr):
    """
        Heapify Array O(N)
        Pop Elements off heap O(NlogN)
    """
    heapq.heapify(arr)
    while len(arr) > 0:
        print(heapq.heappop(arr))

if __name__ == '__main__':
    arr = [3,41,16,6,3,26,72,27,26]
    heapsort(arr)

