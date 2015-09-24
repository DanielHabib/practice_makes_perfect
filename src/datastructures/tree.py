class Tree:
    def __init__(self, node=None):
        self.root = node
        self.nodes = []

    def firstCommonAncestor(a, b):
        """ 4.8
            Take two nodes and find their first common ancestor without
            using any additional datastructures
            Time Complexity: O(log(N)) best case, and O(N) worst case
            Space Complexity: constant
        """
        while a.parent and b.parent:
            if a.isMarked():
                return a
            a.mark()
            if b.isMarked():
                return b
            b.mark()
            a = a.parent
            b = b.parent

        while a.parent:
            if a.marked():
                return a
            a.mark()
            a = a.parent
        while b.parent:
            if b.marked():
                return b
            b.mark()
            b = b.parent
        return None


class Node:
    def __init__(self, val, children=None, parent=None):
        self.val = val
        self.children = children
        self.parent = parent
        self.marked = False

    def mark(self):
        """ Mark the Node """
        self.marked = True

    def isMarked(self):
        """ Check if the Node is Marked """
        return self.marked
