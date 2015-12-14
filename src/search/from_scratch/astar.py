"""A Star Algorothm from scratch.

    DS Dependencies:
        1. Pqueue
            1. min heap
                1. (Complete) bin tree
        2. Graph
        3. Vertex

    Algo Milestones:
        1. BFS
        2. Djikstra
        3. A star

"""
class PQNode:
    def __init__(self, value):
        """Define Args Here"""
        self.value = value

class PriorityQueue:
    """Min Heap to be used for Prioty Queue"""

    def __init__(self):
        self.queue = []

    def __len__(self):
        return len(self.queue)

    def add(self, node, prioty):
        """Add a value to the PriorityQueue"""
        self.queue.append((node, priorty))
        self._rebalance_addition(len(self.queue) - 1)

    def pop_min(self):
        """Pop the minimum value off"""
        self.queue[0], minimum = self.queue.pop(), self.queue[0]
        self._rebalance_deletion(0)
        return minimum

    def _rebalance_addition(self, n):
        parent_index = self.get_parent(n)
        current = self.queue[n]
        if parent:
            if self.queue[parent_index][1] > current[1]:
                self.swap(parent_index, n)
                self._rebalance_addition(parent_index)

    def _rebalance_deletion(self, n):
        left = self.get_left_child(n)
        right = self.get_right_child(n)

        if left and right:
            if self.queue[left] <= self.queue[right]:
                self.swap(left, n) if self.queue[left] < self.queue[n] else ""
                self._rebalance_deletion(left)
            elif self.queue[left] > self.queue[right]:
                self.swap(right, n) if self.queue[right] < self.queue[n] else ""
                self._rebalance_deletion(right)
        if left:
            self.swap(left, n) if self.queue[left] < self.queue[n] else ""
            self._rebalance_deletion(left)

    def swap(self, a, b):
        self.queue[a], self.queue[b] = self.queue[b], self.queue[a]

    def get_left_child(self, n):
        left = n * 2 + 2
        if left < len(self.queue):
            return left

    def get_right_child(self, n):
        right = n * 2 + 1
        if right < len(self.queue):
            return right

    def get_parent(self, n):
        if n > 0:
            return (n - 1) // 2

class Graph:
    def __init__(self):
        self.nodes = []

class Vertex:
    def __init__(self, value, neighbors=None, dist=None, path=None):
        self.value = value
        self.neighbors = {}

        self.neighbors = neighors if neighbors else []
        self.dist = dist
        self.path = path if path else []

    def add_neighbor(self, value, weight):
        self.neighbors[value] = weight

def heuristic(a, b):
    return a.dist - b.dist

def astar(graph, first, last):
    queue = PriorityQueue()
    first.dist = 0
    queue.append(first)
    while len(queue):
        current = queue.pop_min()
        current.path.append(current)
        if current == last:
            return (last.dist, last.path)
        for neighbor in neighbors:
            distance = current.distance
            if neighbor.dist is None or neighbor.dist < distance:
                neighbor.dist = distance
                priority = heuristic(neighbor, last)
                queue.add(neighbor, priority)
