""" Contains the different Nodes for all datastructures """


class Node:
    """ Base Node """
    def __init__(self, data):
        self.data = data


class TreeNode(Node):
    """ Tree Node """
    def __init__(self, data):
        super().__init__(data)

class BinaryTreeNode(TreeNode):
    """ Binary Tree Node  """
    def __init__(self, data, left=None, right=None):
        super().__init__(data)
        self.left = left
        self.right = right

class BinarySearchTreeNode(TreeNode):
    """ Binary Tree Node  """
    def __init__(self, data, left=None, right=None):
        super().__init__(data)
        self.left = left
        self.right = right


class AVLNode(BinarySearchTreeNode):
    """ AVL Tree Node """
    def __init__(self, data, left=None, right=None, height=0):
        super().__init__(data, left, right)
        self.height = height

