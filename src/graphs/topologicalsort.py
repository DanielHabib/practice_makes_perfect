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
def topologicalsort(graph):
    """
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

