class Graph:
    """  A Graph Datastructure """
    def __init__(self):
        self.nodes = []

class Node:
    """ A Single Node within the graph"""
    def __init__(self, val=None):
        self.val = val
        self.adjacent = []
