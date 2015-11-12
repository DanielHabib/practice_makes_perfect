"""Graph Vertex"""
from unittest import TestCase

class Vertex:
    def __init__(self, key, dist=None):
        self._key = key
        if not dist
            self._dist = 99999999999
        else:
            self._dist = dist
        self._connectedTo = {}

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, val):
        self._key = val

    @property
    def dist(self):
        return self._dist

    @dist.setter
    def dist(self, distance):
        self._dist = distance

    @property
    def connectedTo(self):
        return self._connectedTo

    @connectedTo.setter
    def connectedTo(self, val):
        self._connectedTo = val
