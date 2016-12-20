"""
{
    "H": ["G", "E", "C", "A"],
    "G": ["E", "D", "F"]
    "F": ["E", "B", "A"]
    "E": ["D", "C", "B", "A"],
    "D": ["C"],
    "C": ["B", "A"],
    "B": ["A"],
    "A": [],
}

"""


def topologicalsort2(graph):
    """
    THIS SHOULD BE SOLVED WITH DFS SOMEHOW
    This is solving a graph dependency thing, if the graph is reveresed. Lets see if we can print a reverse chron list
        We can only do topological sorts on DAGs
        We should be sure to check that it is not acyclic

        WRONG. Predessocors point to things 
    """
    graphC = graph.copy()
    sortedSet = []
    valsToDelete = []
    while len(graphC):
        acyclic = False
        for nodeVal, neighbors in graphC.items():
            for neighbor in neighbors:
                if neighbor in sortedSet:
                    neighbors.remove(neighbor)
            if neighbors == []:
                acyclic = True
                sortedSet.append(nodeVal)
                valsToDelete.append(nodeVal)

        if not acyclic:
            print(graphC)
            print(sortedSet)
            print(valsToDelete)
            raise Exception()
            
        for value in valsToDelete:
            del(graphC[value])
        valsToDelete = []

    return sortedSet


def topologicalsort(graph):
    
    visited = set()


    def dfs(node, stack, visited, graph):
        if node:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor, stack, visited, graph)
            stack.append(node)
    stack = []
    for node in graph.keys():
        if node not in visited:
            dfs(node, stack, visited, graph)
    return stack[::-1]

if __name__ == '__main__':

    graph = {
        "H": ["G", "E", "C", "A"],
        "G": ["E", "D", "F"],
        "F": ["E", "B", "A"],
        "E": ["D", "B", "A"],
        "D": ["C"],
        "C": ["B", "A"],
        "B": ["A"],
        "A": [],
    }
    print(topologicalsort(graph))

