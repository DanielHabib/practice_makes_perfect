"""Graph Vertex"""
from unittest import TestCase

class Vertex:
    def __init__(self, key, value, dist=None):
        self._key = key
        self.dist = dist if dist else 999999999999
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getWeight(self, nbr):
        return self.connectedTo[nbr]


