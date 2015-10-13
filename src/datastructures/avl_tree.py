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
        self.nodes = []
        self.height = height
        if root:
            self.root = AVLNode(root)
            self.nodes.append(root)
        else:
            self.root = None


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
        if type(data) is list:
            for val in data:
                self.inject(val)
            return True

        if not self.root:
            self.root = AVLNode(data)
            self.nodes.append(self.root)
            return True

        if (self.inject_helper(self.root, data)):
            self.rebalance()
            return True

    def inject_helper(self, current_node, data):
        """ Binary Search Tree Injection """
        if data == current_node.data:
            raise DuplicateNodeError
        if data < current_node.data:
            if not current_node.left:
                new_node = AVLNode(data)
                current_node.left = new_node
                self.nodes.append(new_node)
            else:
                self.inject_helper(current_node.left, data)
        else:
            if not current_node.right:
                new_node = AVLNode(data)
                current_node.right = new_node
                self.nodes.append(new_node)
            else:
                self.inject_helper(current_node.right, data)

    def rebalance(self):
        pass

    def in_order(self, verbose=False):
        """ In Order Traversal 
        
            Returns a list of nodes in order traversal
        """
        if not self.root:
            return []
        alist = []
        self.in_order_helper(self.root, alist, verbose)
        return alist

    def in_order_helper(self, node, alist=[], verbose=False):
        """
            Handles the recursion associated with in order traversal
        """
        if node:
            in_order_helper(node.left, alist)
            if verbose:
                print(node.data)
            alist.append(node)
            in_order_helper(node.right, alist)
            

    def pre_order(self, verbose=False):
        """ In Pre Traversal 
        
            Returns a list of nodes pre order traversal
        """
        if not self.root:
            return []
        alist = []
        self.pre_order_helper(self.root, alist, verbose)
        return alist

    def pre_order_helper(self, node, alist=[], verbose=False):
        """
            Handles the recursion associated with pre order traversal
        """
        if node:
            if verbose:
                print(node.data)
            alist.append(node)
            pre_order_helper(node.left, alist, verbose)
            pre_order_helper(node.right, alist, verbose)
            
    def post_order(self, verbose=False):
        """ In Post Traversal 
        
            Returns a list of nodes pre order traversal
        """
        if not self.root:
            return []
        alist = []
        self.pre_order_helper(self.root, alist, verbose)
        return alist

    def post_order_helper(self, node, alist=[], verbose=False):
        """
            Handles the recursion associated with post order traversal
        """
        if node:
            pre_order_helper(node.left, alist, verbose)
            pre_order_helper(node.right, alist, verbose)
            if verbose:
                print(node.data)
            alist.append(node)

    def __repr__(self):
        return self.nodes;


class TestAVLTree(TestCase):
    """ Test the avl tree to ensure proper behavior """

    def test_inject_on_empty_tree_sets_root(self):
        """ Insert Root Node """
        tree = AVLTree()
        tree.inject(1)
        self.assertEquals(tree.root.data, 1)

    def test_inject_right(self):
        """ Insert Right Child """
        tree = AVLTree()
        tree.inject(1)
        tree.inject(3)
        self.assertEquals(tree.root.right.data, 3)

    def test_inject_left(self):
        """ Insert Left Child """
        tree = AVLTree()
        tree.inject(3)
        tree.inject(1)
        self.assertEquals(tree.root.left.data, 1)
    
    def test_create_tree_with_data(self):
        """ Create Tree With Node """
        tree = AVLTree(1)
        self.assertEquals(tree.root.data, 1)
    
    def test_nodes_properties_populates(self):
        """ Ensure Nodes Property is Populated """
        tree = AVLTree()
        injection_list = [3,1,4,5,64,2,74,234,2131,123]
        for val in injection_list:
            tree.inject(val)
        self.assertEquals([x.data for x in tree.nodes], injection_list)

    def test_create_with_list(self):
        """ Create a Tree With A List of Values """
        injection_list = [3,4,2,51,5,43,1,3214,6]
        tree = AVLTree()
        tree.inject(injection_list)
        self.assertEquals([x.data for x in tree.nodes], injection_list)

    def test_duplicate_val_raises_error(self):
        """ Ensure DuplicateNodeError is Raised """
        tree = AVLTree()
        tree.inject(3)
        with self.assertRaises(DuplicateNodeError):
            tree.inject(3)

    def test_in_order(self):

