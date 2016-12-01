"""
The Graph abstract data type defines the following interface:

    adjacent(x, y): tests whether there is an edge from the vertices x to y;
    neighbors(x): lists all vertices y such that there is an edge from the vertices x to y;

    add_vertex(x): adds the vertex x, if it is not there;V
    remove_vertex(x): removes the vertex x, if it is there;

    add_edge(x, y): adds the edge from the vertices x to y, if it is not there;
    remove_edge(x, y): removes the edge from the vertices x to y, if it is there;

    get_vertex_value(x): returns the value associated with the vertex x;
    set_vertex_value( x, v): sets the value associated with the vertex x to v.

    Structures that associate values to the edges usually also provide:[1]
    get_edge_value(x, y): returns the value associated with the edge (x, y);
    set_edge_value( x, y, v): sets the value associated with the edge (x, y) to v.

As a result all support BFS/DFS/A*/Djkstra Traversals and Topological Sorting

We will be listing out 3 Different Implementations of the graph.
    1. Adjacent Matrix
    2. Adjacency Lists
    3. Nodes and Pointers



"""

from vertex import Vertex
import numpy


class AdjacencyMatrixGraph:
    """a
        An adjacency matrix graph datastructure. 
        Every function will contain its runtime
        The structure as a whole takes up O(N^2) space 



        Personally, I wouldnt use an adjacency matrix implementation to represent a graph unless I hada fixed number of vertexes AND a strict need for constant time edge mutation and lookup........... Also I would want it to be dense.
    """
    def __init__(self, n):
        """
        n: int, contains the initial size of the matrix. (make it large, try to avoid the need to resize without going to big)
        """
        self.mapping = {}
        self.graph = numpy.zeros([n, n])
        self.vertexList = []
        
    def adjacent(self, x, y):
        xIndex = self.getIndex(x)
        yIndex = self.getIndex(y)
        return bool(self.graph[xIndex, yIndex])

    def neighbors(self, x):
        xIndex = self.getIndex(x)
        neighborIndexes = self.graph(xIndex, :)
        return [self.vertexList[i] for i, x in enumerate(neighborIndexes) if x != 0]
    
    def add_edge(self, x, y):
        source = self.getIndex(x)
        destination = self.getIndex(y)
        self.matrix[source, destination] = 1

    def remove_edge(self, x, y):
        source = self.getIndex(x)
        destination = self.getIndex(y)
        self.matrix[source, destination] = 0

    def add_vertex(self, x):
        self.vertexList.append(x)

    def get_vertex_index(self, x):
        for index, value in enumerate(self.vertexList):
            if value == x:
                return index


class Graph:
    """A Graph Abstract Datastructure implemented w/ Nodes and pointers
    
    """
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


