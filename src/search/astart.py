"""A star
    Pretty Much just Breadth First Search with a priority Queue
"""
from datastructures.graph import Graph
from datastructures.priority_queue import PriorityQueue
from datastructures.vertex import Vertex

def a_star(graph, start, goal):
    """Get the distance between the start and the final node"""
    pq = PriorityQueue()
    pq.buildHeap(graph)
    start.distance = 0
    while not pqueue.isEmpty():
        currentVert = pqueue.pop()
        if currentVert == goal:
            break
        for nextVert in currentVert.connectedTo:
            newdist = currentVert.dist + currentVert.getWeight(nextVert)
            if newdist < nextVert.dist:
                nextVert.dist = newdist
                priority = heuristic(nextVert, goal)
        return currentVert.dist

def heuristic(node, final):
    """Whatever the heuristic function represents"""
