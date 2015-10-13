""" An Avl tree that balances a tree as nodes are added on """
from node import AVLNode

from unittest import TestCase


class DuplicateNodeError(Exception):
    """ Attempted to enter a duplicate node """

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
                new_node = AVLNode(data)
                current_node.left = new_node
                self.nodes.append(new_node)
            return self.inject_helper(current_node.left, data)
        else:
            if not current_node.right:
                new_node = AVLNode(data)
                current_node.right = new_node
                self.nodes.append(new_node)
            return self.inject_helper(current_node.right, data)


    def rebalance(self):
        pass

    def __repr__(self):
        return self.nodes;


class TestAVLTree(TestCase):
    """ Test the avl tree to ensure proper behavior """

    def test_inject_on_empty_tree_sets_root(self):
        """ Be sure that we can inject """
        tree = AVLTree()
        tree.inject(1)
        self.assertEquals(tree.root.data, 1)

    def test_inject_right_node(self):
        """ To ensure that nodes are placed in the right side correctly """
        tree = AVLTree()
        tree.inject(1)
        tree.inject(3)
        self.assertEquals(tree.root.right.data, 3)









