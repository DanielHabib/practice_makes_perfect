from vertex import Vertex


class Graph:
    """A Graph Datastructure"""
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices += 1
        new_vertex = Vertex(key)
        self.vertList[key] = newVertex
        return new_vertex

    def getVertex(self, key):
        return self.vertList.get(key, None)

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, f, t, cost=0):
        if f not in self.vertList:
            root = self.addVertex(f)
        if t not in self.vertList:
            destination = self.addVertex(t)
        root.addNeighor(destination)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())



