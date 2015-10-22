"""Dynamic Programming, Shortest Path

Used Frequently in finding the min and max
"""


"""Notes About Shortest Path Prob
        s -> u -> v
        ∂(s, v) = min{∂(s, u) + w(u, v)}

    What is a DAG?
    Directed Acyclic Graph, I'm glad you asked

    When given a DAG we can simply use memoization to make it Dynamic
    Example of using memoization on a DAG
"""

class ShortestPathResult:
    def __init__(self):
        self.d = {}
        self.parent = {}

def shortest_path(graph, s):
    """Single source shortest paths using DP on a DAG

    Args:
        graph: weighted DAG
        s: source
    """
    result = ShortestPathResult()
    result.d[s] = 0
    result.parent[s] = None
    for v in graph.itervertices():
        sp_dp(graph, v, result)
        return result

def sp_dp(graph, v, result):
    """Recursion on finding the shortest path to v

    Args:
        graph: weight DAG
        v: a vertex in the graph
        result: for memoization and keeping track of the result

    LTE: for an Directed Acyclic Graph, we store something somewhere
    """
    """
        MEMO CHECK
    """
    if v in result.d:
        return result.d[v]
    result.d[v] = float('inf')
    result.parent[v] = None
    for u in graph.inverse_neighbors(v):
        new_distance = sp_dp(graph, u, result) + graph.weight(u, v)
        if new_distance < result.d[v]:
            result.d[v] = new_distance
            result.parent[v] = u
    return result.d[v]

