""" An Avl tree that balances a tree as nodes are added on """
from node import AVLNode

class DuplicateNodeError(Exception):
    """ """

class AVLTree:
    """ AVL Tree that is self balancing
        This AVL tree doesn't allow for duplicates
    """
    def __init__(self, root=None, height=0):
        self.root = AVLNode(root)
        self.nodes = []
        self.height = height


    def inject(self, data):
        """
            A function that adds nodes to the tree while maintaining
            a balance factor of 1

            balance factor = abs(self.left.height - self.right.height)
            This function assumes that the tree is balanced prior to
            injection
        4 cases:
            1. LL rotation

        """
        if not self.root:
            self.root = AVLNode(data)
            return True

        if (self.inject_helper(node, data)):
            self.rebalance()
            return True


    def inject_helper(self, current_node, data):
        """ Binary Search Tree Injection """
        if data == current_node.data:
            raise DuplicateNodeError
        if current_node.data < data:
            if not current_node.left:
                current_node.left = AVLNode(data)
            return self.inject_helper(current_node.left, data)
        else:
            if not current_node.right:
                current_node.right = AVLNode(data)
            return self.inject_helper(current_node.right, data)


    def rebalance(self):








