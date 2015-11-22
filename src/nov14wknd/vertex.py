class Vertex:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
    def add_connection(self, node, weight):
        self.neighbors[node] = weight

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node, weight=0):
        self.nodes[node] = weight
