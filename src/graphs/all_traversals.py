"""
Dijkstra & Primms
"""
from enum import Enum
from collections import deque
from unittest import TestCase
from pprint import pprint as pp
import heapq


class Color:
    WHITE = "white" 
    GREY = "grey"
    BLACK = "black"


class Node:
    def __init__(self, val, neighbors=None, parent=None, color=Color.WHITE, distance=0):

        if neighbors is None: neighbors = {}

        self.__dict__.update({x:k for x,k in locals().items() if x != 'self'})
    
    def addNeighbor(self, neighbor, weight=0):
        self.neighbors[neighbor] = weight

class Graph:
    def __init__(self, nodes=None):
        if nodes is None: nodes = []
        self.nodes = nodes
    
    def getStartNode(self):
        """This method is in support of testing to allow us to consistently and easily get the `A` node. 
        While this introduces a lack of variety in our test suite because it would be more robust to test multiple different nodes as starts, 
        I only manually worked out cases for traversals starting at this node.
        """
        for node in self.nodes:
            if node.val == "a":
                return node
    

    def refreshGraph(self):
        for node in self.nodes:
            node.color = Color.WHITE
            node.distance = 0
            node.parent = None

    def buildWeightedFromDictionary(self, nodes, countsOn=False):
        nodeList = {}
        for value in nodes.keys():
            node = Node(value)
            nodeList[value] = node
            self.addNode(node)
        
        for value, neighbors in nodes.items():
            currentNode = nodeList[value]
            for neighbor in neighbors:
                currentNode.addNeighbor(nodeList[neighbor[0]], neighbor[1])

    def buildUnweightedUndirectedFromDictionary(self, nodes):
        nodeList = {}
        for value in nodes.keys():
            node = Node(value)
            nodeList[value] = node
            self.addNode(node)
        
        for value, neighbors in nodes.items():
            currentNode = nodeList[value]
            for neighbor in neighbors:
                currentNode.addNeighbor(nodeList[neighbor])    

    def getPath(self, node):
        path = []
        self._getPath(node, path)
        return path

    def _getPath(self, node, path):
        if node.parent:
            self._getPath(node.parent, path)
        path.append(node)

    def repGraph(self, sortAttr="distance"):
        sortedNodes = sorted(self.nodes, key=lambda x:getattr(x, sortAttr))
        graphRep = []
        
        return [
                {
                    "val":node.val, 
                    "parent":node.parent.val if node.parent else None, 
                    "neighbors": list(map(lambda n:n.val, node.neighbors)),
                    "color": node.color, 
                    "distance": node.distance
                } for node in sortedNodes]

    def addNode(self, node):
        self.nodes.append(node)
         
    def primms(self, start):
        # Updating the Heap in place
        pqueue = []
        tree = []
        nodeDict = {}
        heapq.heappush(pqueue, (0, 0, start))
        start.color = Color.GREY
        i = 1
        while len(pqueue) > 0:
            _, count, current = heapq.heappop(pqueue)

            if current.color == Color.BLACK:
                continue

            if current.parent:
                tree.append((current.parent.val, current.val))

            for neighbor, weight in current.neighbors.items():
                if neighbor.color != Color.BLACK and nodeDict.get(neighbor, float('inf')) > weight:
                    
                    neighbor.color = Color.GREY
                    neighbor.distance = weight
                    neighbor.parent = current
                    nodeDict[neighbor] = weight

                    heapq.heappush(pqueue, (weight, i,  neighbor))

                    i += 1
            current.color = Color.BLACK
        return tree               

    def dijkstras(self, start):
        start.color = Color.GREY
        pqueue = []
        heapq.heappush(pqueue, (0, start))

        while len(pqueue) > 0:
            _, current = heapq.heappop(pqueue)
            if current.color == Color.BLACK:
                continue
            for neighbor, weight in current.neighbors.items():
                neighborDistance = current.distance + weight

                if neighbor.color != Color.BLACK and (neighbor.distance == 0 or neighbor.distance > neighborDistance):

                    neighbor.distance = neighborDistance
                    neighbor.color = Color.GREY
                    neighbor.parent = current

                    heapq.heappush(pqueue, (neighborDistance, neighbor))
            current.color = Color.BLACK

    def dfs(self, start):
        """
            Dfs doesn't guarentee the shortest path, so there is no point in testing that or updating distance. Instead we just want to see that they all get processed
        """
        for neighbor in start.neighbors:
            if neighbor.color == Color.WHITE:
                neighbor.color = Color.GREY
                self.dfs(neighbor)
        start.color = Color.BLACK

    def bfs(self, start):
        """<<<Ignore the weights of the Edges>>>"""
        start.color = Color.GREY
        queue = deque()
        queue.append(start)
        while len(queue) > 0:
            currentNode = queue.popleft()
            for neighbor in currentNode.neighbors.keys():
                if neighbor.color == Color.WHITE:
                    neighbor.parent = currentNode
                    neighbor.distance = currentNode.distance + 1
                    neighbor.color = Color.GREY
                    queue.append(neighbor)
            currentNode.color = Color.BLACK

    def topologicalSort(self):
        arranged = []
        for node in self.nodes:
            if node.color == Color.WHITE:
                self.topSortHelper(node, arranged)

        return arranged[::-1]

    def topSortHelper(self, node, arranged):
        node.color = Color.GREY
        for neighbor in node.neighbors:
            if neighbor.color == Color.GREY:
                raise Exception("Cycle Detected")
            if neighbor.color == Color.WHITE:
                self.topSortHelper(neighbor, arranged)
        node.color = Color.BLACK
        arranged.append(node.val)

class TopologicalSortTest(TestCase):
    def setUp(self):
        # Graph is undirected w.o weights
        graph = Graph()
        graph.buildUnweightedUndirectedFromDictionary({
                    "a": ["b", "c", "d"],
                    "b": ["c", "e"],
                    "c": ["e", "g"],
                    "d": ["b"],
                    "e": ["f"],
                    "f": [],
                    "g": ["e"],
                })
        self.graph = graph
        self.trueArray = [True] * len(self.graph.nodes)
        self.result = self.graph.topologicalSort()

    def test_topsort_all_nodes_processed(self):
        self.assertEquals([x["color"] == Color.BLACK for x in  self.graph.repGraph()], self.trueArray)

    def test_topsort_returns_valid_order(self):
        self.assertEquals(self.result, ['a', 'd', 'b', 'c', 'g', 'e', 'f'])

class PrimmsTest(TestCase):
    def setUp(self):
        # Graph is undirected w.o weights
        graph = Graph()
        graph.buildWeightedFromDictionary({
                    "a": [("b", 12), ("c", 3), ("d", 6)],
                    "b": [("d", 5), ("c",18), ("a", 12), ("e", 8)],
                    "c": [("a", 3), ("b", 18), ("g", 4)],
                    "d": [("a", 6), ("b", 5)],
                    "e": [("b", 8), ("g", 6), ("f", 4)],
                    "f": [("e", 4)],
                    "g": [("c", 4), ("e", 6)],
                })
        self.graph = graph
        self.trueArray = [True] * len(self.graph.nodes)
        start = self.graph.getStartNode()
        self.tree = self.graph.primms(start)

    def test_primms_all_nodes_processed(self):
        self.assertEquals([x["color"] == Color.BLACK for x in  self.graph.repGraph()], self.trueArray)

    def test_primms_returns_correct_tree(self):
        self.assertEquals(self.tree, [('a', 'c'), ('c', 'g'), ('a', 'd'), ('d', 'b'), ('g', 'e'), ('e', 'f')])

class DijkstraTest(TestCase):
    def setUp(self):
        # Graph is undirected w.o weights
        graph = Graph()
        graph.buildWeightedFromDictionary({
                    "a": [("b", 12), ("c", 3), ("d", 6)],
                    "b": [("c",18), ("a", 12), ("e", 8)],
                    "c": [("a", 3), ("b", 18), ("g", 4)],
                    "d": [("a", 6), ("b", 5)],
                    "e": [("b", 8), ("g", 6), ("f", 4)],
                    "f": [],
                    "g": [("c", 4), ("e", 6)],
                })
        self.graph = graph
        self.trueArray = [True] * len(self.graph.nodes)
        start = self.graph.getStartNode()
        self.graph.dijkstras(start)

    def test_dijkstra_all_nodes_processed(self):
        self.assertEquals([x["color"] == Color.BLACK for x in  self.graph.repGraph()], self.trueArray)


    def test_dijkstra_all_nodes_have_correct_distance(self):
        distances = {
            "a": 0,
            "b": 11,
            "c": 3,
            "d": 6,
            "e": 13,
            "f": 17,
            "g": 7
        }
        graphRep = self.graph.repGraph("val")
        self.assertEquals(
                [node["distance"] == distances[node["val"]] for node in graphRep],
                self.trueArray)

    def test_dijsktra_path_works(self):
        fNode = None
        for node in self.graph.nodes:
            if node.val == "f":
                fNode = node
        rawPath = self.graph.getPath(fNode)
        path = [x.val for x in rawPath]
        self.assertEquals(path, ["a", "c", "g", "e", "f"])



class DFSGraphTest(TestCase):
    def setUp(self):
        # Graph is undirected w.o weights
        graph = Graph()
        graph.buildUnweightedUndirectedFromDictionary({
                    "a": ["b", "c", "d"],
                    "b": ["d", "c", "a", "e"],
                    "c": ["a", "b", "g"],
                    "d": ["a", "b"],
                    "e": ["b", "g", "f"],
                    "f": ["e"],
                    "g": ["c", "e"],
                })
        self.graph = graph
        self.trueArray = [True] * len(self.graph.nodes)
        start = self.graph.getStartNode()
        self.graph.dfs(start)
    def test_dfs_all_nodes_black(self):
        self.assertEquals(
                [x["color"] == Color.BLACK for x in self.graph.repGraph()],
                self.trueArray)


class BFSGraphTest(TestCase):
    def setUp(self):
        # Graph is undirected w.o weights
        graph = Graph()
        graph.buildUnweightedUndirectedFromDictionary({
                    "a": ["b", "c", "d"],
                    "b": ["d", "c", "a", "e"],
                    "c": ["a", "b", "g"],
                    "d": ["a", "b"],
                    "e": ["b", "g", "f"],
                    "f": ["e"],
                    "g": ["c", "e"],
                })
        self.graph = graph
        self.trueArray = [True] * len(self.graph.nodes)
        start = self.graph.getStartNode()
        self.graph.bfs(start)

    def test_dfs_all_nodes_black(self):
        self.assertEquals(
                [x["color"] == Color.BLACK for x in self.graph.repGraph()],
                self.trueArray)

    def test_bfs_all_nodes_have_correct_distance(self):
        distances = {
            "a": 0,
            "b": 1,
            "c": 1,
            "d": 1,
            "e": 2,
            "f": 3,
            "g": 2
        }
        graphRep = self.graph.repGraph("val")
        self.assertEquals(
                [node["distance"] == distances[node["val"]] for node in graphRep],
                self.trueArray)

    def test_bfs_path_works(self):
        fNode = None
        for node in self.graph.nodes:
            if node.val == "f":
                fNode = node
        rawPath = self.graph.getPath(fNode)
        path = [x.val for x in rawPath]
        self.assertEquals(path, ["a", "b", "e", "f"])

        
if __name__ == '__main__':
    # BFS
    graph = Graph()

