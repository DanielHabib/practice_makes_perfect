""" 4.1 Routes Between Nodes  """


def search(n1, n2):
    """
        args:
            n1 and n2 are two separate nodes in a graph, we want to find if
            there is a path between the two
        Assumptions:
            Since it is a 'directed' graph then I would assume we have to
            find the path starting on one side at a time. We would need to
            check from N1 to N2 then check from N2 to N1
        BCR: O(N)
        Time Complexity: O(N)
        Space Complexity: O(N)
    """
    queue = Queue()
    n1.marked = True

    queue.enqueue(n1)
    while not queue.isEmpty():
        current = queue.dequeue()
        if visitAndCheck(current, n2):
            return True
        for node in current.adjacent:
            if node.marked == False:
                node.marked = True
                queue.enqueue(node)

    queue.enqueue(n2)
    while not queue.isEmpty():
        current = queue.dequeue()
        if visitAndCheck(current, n1):
            return True
        for node in current.adjacent:
            if node.marked == False:
                node.marked = True
                queue.enqueue(node)
    return False


def visitAndCheck(node, node2):
    if node == node2:
        return True
    else:
        return False
