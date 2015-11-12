from unittest import TestCase
"""Dijkstra
    Pretty Much just Breadth First Search with a priority Queue
"""
from datastructures.priority_queue import PriorityQueue
from datastructures.vertex import Vertex
from datastructures.graph import Graph


def dijkstra(agraph, goal):
    pq = PriorityQueue()
    start.setDistance(0)
    for val in agraph:
        pq.add(val)
    dist = 0
    while not pq.isEmpty():
        currentVert = pq.pop()
        for nextVert in currentVert.connectedTo:
            newDist = currentVert.distance + currentVert.getWeight(nextVert)
            if newDist < nextVert.distance:
                nextVert.distance = newDist
                nextVert.pred = currentVert
