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
    def __init__(self, data, left=None, right=None, height=1, parent=None):
        super().__init__(data, left, right)
        self.height = height
        self.parent = parent

    @property
    def balance_factor(self):
        return self._calculate_balance_factor()

    def _calculate_balance_factor(self):
        left = 0
        right = 0
        if self.left:
            left = self.left.height
        if self.right:
            right = self.right.height
        return left - right

    def isLeftChild(self):
        return self.parent.left == self

    def isRightChild(self):
        return self.parent.right == self



















