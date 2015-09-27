import random
""" 4.11 Random Node """

"""
    Implement a binary tree from scratch, in addition to
    insert, find, delete create a method `getRandomNode()` which
    returns a random node from the tree. All nodes should be equally likely
    to be chosen. Design and implement an algorithm for getRandomNode
    and explani how you wuold implement the rest of the methods

    Steps:
        1. Create BinaryTree
        2. Create Node
        3. Create methods: insert, find, delete
        4. create getRandomNode

"""
class EmptyNodeError(Exception):
    """ Nodes must have a value in order to be inserted into a tree """

class InvalidChildrenError(Exception):
    """ When Adding a node to a tree, it cannot have children"""

class NodeNotFoundError(Exception):
    """ Unable to find the specific node in the tree"""


class BinaryTree:
    """ Binary Tree """
    def __init__(self, root=None):
        self.root = None
        self.nodes = []
        if root:
            self.nodes.append(root)

    def insert(self, node):
        """ User Facing Insert Function """
        if not node or node.val == None:
            raise EmptyNodeError("Cannot add an empty Node")
        if node.leftChild or node.rightChild:
            raise InvalidChildrenError("Node to be added cannot"\
                                        "have children")
        if not self.root:
            self.root = node
            return True
        return _insert_helper(self.root, node)

    def _insert_helper(self, treeNode, node):
        """ Recursion element of the insert function """
        if treeNode.val >= node.val:
            if not treeNode.leftChild:
                treeNode.leftChild = node
                self.nodes.append(node)
                return True
            _insert_helper(treeNode.leftChild, node)
        elif treeNode.val < node.val:
            if not treeNode.rightChild:
                treeNode.rightChild = node
                self.nodes.append(node)
                return True
            _insert_helper(treeNode.rightChild, node)

    def find(self, val):
        """ Find a node that matches the given value then return that node
        """
        return _find_helper(None, self.root, val)

    def _find_helper(self, parent, treeNode, val):
        """ Handle the recurison associated with finding a node """
        if treeNode.val == val:
            return (parent, treeNode)

        elif treeNode.val > val:
            if not treeNode.leftChild:
                return False
            return _find_helper(treeNode, treeNode.leftChild, val)

        elif treeNode.val < val:
            if not treeNode.rightChild:
                return False
            return _find_helper(treeNode, treeNode.rightChild, val)

    def delete(self, val):
        """
            1. find the node with the value
            2. use the removal function

            TBR = To be removed
        """
        nodeTBR = self.find(val)
        if not nodeTBR:
            raise NodeNotFoundError()
        self.remove(parent, nodeTBR)

    def remove(self, parent, nodeTBR):
        """
            Handle all 3 cases when deleting a node:
                0 children
                1 child
                2 children
        """

        """ 0 Children Case """
        if nodeTBR.leftChild == None and nodeTBR.rightChild == None:
            return _removeWithNoChildren(parent, nodeTBR)
        """ 2 Children Case """
        if nodeTBR.leftChild and nodeTBR.rightChild:
            return _removeWithTwoChildren
        """ 1 Child Case """
        if nodeTBR.leftChild or nodeTBR.rightChild:
            return _removeWithOneChild
        return False

    def _removeWithNoChildren(self, parent, nodeTBR):
        if parent.leftChild == nodeTBR:
            parent.leftChild = None
        elif parent.rightChild == nodeTBR:
            parent.rightChild = None
        self.nodes.pop(nodeTBR)
        return True

    def _removeWithOneChild(self, parent, nodeTBR):
        validChild = None
        if nodeTBR.leftChild:
            validChild = nodeTBR.leftChild
        else:
            validChild = nodeTBR.rightChild
        if nodeTBR.leftChild or nodeTBR.rightChild:
            if parent.leftChild == nodeTBR:
                parent.leftChild = validChild
            elif parent.rightChild == nodeTBR:
                parent.rightChild = validChild
            self.nodes.pop(nodeTBR)
            return True

    def _removeWithTwoChildren(self, parent, nodeTBR):
        replacementNode = removeWithTwoChildren(parent, nodeTBR.rightChild)

        if parent.leftChild == nodeTBR:
            parent.leftChild = replacementNode
            replacementNode.rightChild = nodeTBR.rightChild
            replacementNode.leftChild = nodeTBR.leftChild
        if parent.rightChild == nodeTBR:
            parent.rightChild = replacementNode
            replacementNode.rightChild = nodeTBR.rightChild
            replacementNode.leftChild = nodeTBR.leftChild
        self.nodes.pop(nodeTBR)
        return True

    def _removeWithTwoHelper(self, parent, node):
        if not node.leftChild:
            parent.leftChild = None
            return node
        _removeWithTwoHelper(node, node.leftChild)

    def randomNode(self):
        return = self.nodes[randrange(0, len(self.nodes.length)-1)]


class Node:
    def __init__(self, val, leftChild=None, rightChild=None):
        self.val = val
        self.leftChild = leftChild
        self.rightChild = rightChild
