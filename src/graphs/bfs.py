"""
BFS

"""
from unittest import TestCase
class GraphNode:
    def __init__(self, key, value, distance=None, neighbors=None, parent=None):
        if neighbors is None:
            neighbors = {}
        self.__dict__.update({x :k for x, k in locals().items() if x != 'self'})
    


def bfs(start, searchKey):
    """
    start: GraphNode
    """
    start.distance = 0
    queue = []
    queue.append(start)
    distance = 0
    while len(queue) > 0:
        current = queue.pop(0)
        if current.key == searchKey:
            return current.value
        for neighbor in current.neighbors:
            if neighbor.distance is None or neighbor.distance > current.distance + 1:
                neighbor.distance = current.distance + 1
                neighbor.parent = current
                queue.append(neighbor)
     return None

def dfs(start, searchKey):
    if start:
        if start.key == searchKey:
            return True
        for neighbor in start.neighbors:
            if neighbor.distance is None or neighbor.distance > start.distance + 1:
                value = dfs(neighbor, searchKey):
                if value:
                    return value
            
def djiskra(start, searchKey):
    start.distance = 0
    pqueue = queue()
    pqueue.push(start.distance, start)
    while len(pqueue) > 0:
        current = pqueue.extractMin()
        if current.key = searchKey:
            return current
        for pathWeight, neighbor in current.neighbors:
            if neighbor.distance is None or neighbor.distance > current.distance + pathWeight:
                neighbor.parent = current
                neighbor.distance = current.distance + pathWeight
                pqueue.push(neighbor.distance, neighbor)

def astart(start, searchKey, heuristicFunc):

    start.distance = 0
    pqueue = queue()
    startRating = heuristicFunc(start)
    pqueue.push(startRating, start)
    while len(pqueue) > 0:
        current = pqueue.extractMin()
        if current.key = searchKey:
            return current.distance
        for pathWeight, neighbor in current.neighbors:
            if neighbor.distance is None or neighbor.distance > current.distance + pathWeight:
                neighbor.parent = current
                neighbor.distance = current.distance + pathWeight
                rating = heuristicFunc(current)
                pqueue.push(rating, neighbor)


 class TestBfs(TestCase):
     def test_bfs(self)





