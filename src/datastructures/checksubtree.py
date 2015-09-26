""" 4.10 Check Subtree """
"""
    Notes:
        T1 & T2 are very large binary trees, and T1 is much bigger than T2.
        Check if T2 is a subtree of T1.

        2 Binary Trees, basically, we must find the root value of T2 in T1.

        What is the fastest way?
        Depth v Breadth?
            Without any more info we can't determine which search method
            would prevail, if it was a bst we could just search that way,
            maybe the best bet would be to do a bfs in order to find it.

    Questions:
        1. Do they have to be the exact same nodes, or just share the same
            value

    Steps;
        1.Implement BFS to find the root node || TC:O(**)
        2.Traverse both trees and be sure that they match completely. || O(t2)


    Time Complexity: O(X), no idea what it is for breadth first search.
    Space Complexity: Since we are doing BFS, we will not be making use of
                    recursion, the only accesory space needed would be the
                    space in the queue.
"""

def checkSubtree(t1, t2):
    """ Check that t2 is a subtree of t1 """
    root1 = t1.root
    root2 = t2.root
    queue = Queue()
    root1.mark = True
    queue.enqueue(root1)
    root2Found = False
    while not queue.isEmpty():
        current = queue.dequeue()
        visit(current, root2)
        for child in current.children:
            if not child.mark:
                child.mark = True
                queue.enqueue(child)


def visit(node1, node2):
    """ Do the visitation of the node """
    if node1.val == node2.val:
        checkTrees(node1, node2)


def checkTrees(node1, node2):
    """
        Loop through the subtrees and be sure they are equal
    """
    if not node1 && not node2:
        return True
    if node1 == node2:
        val1 = checkTrees(node1.left, node2.left)
        val2 = checkTrees(node1.right, node2.right)
        return val2 && val1
    else:
        return False
