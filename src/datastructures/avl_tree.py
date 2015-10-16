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

        self.inject_helper(self.root, data)
        return True

    def inject_helper(self, current_node, data):
        """ Binary Search Tree Injection """
        if data == current_node.data:
            raise DuplicateNodeError
        if data < current_node.data:
            if not current_node.left:
                """ End of the Road """
                new_node = AVLNode(data)
                current_node.left = new_node
                new_node.parent = current_node
                self.nodes.append(new_node)
            else:
                """ Keep Looking """
                self.inject_helper(current_node.left, data)
            current_node.height = current_node.left.height + 1
        else:
            if not current_node.right:
                """ End of the Road """
                new_node = AVLNode(data)
                current_node.right = new_node
                new_node.parent = current_node
                self.nodes.append(new_node)
            else:
                """ Keep Looking """
                self.inject_helper(current_node.right, data)
            current_node.height = current_node.right.height + 1

        if abs(current_node.balance_factor) > 1:
            self.rebalance(current_node)

    def rebalance(self, current_node):
        """ Initiate a Rebalance """
        if current_node.balance_factor > 1:
            """ Left Heavy """
            if current_node.left.balance_factor < 0:
                self._double_right_rotation(current_node)
            else:
                self._single_right_rotation(current_node)
            self._recalculate_height(current_node.parent)
        elif current_node.balance_factor < 1:
            """ Right Heavy """
            if current_node.right.balance_factor > 0:
                self._double_left_rotation(current_node)
            else:
                self._single_left_rotation(current_node)
            self._recalculate_height(current_node.parent)

    def _single_right_rotation(self, current_node):
        """ Handles a right rotation """
        new_root = current_node.left
        parent = current_node.parent

        new_root.parent = parent
        current_node.left = new_root.right
        if current_node.left:
            current_node.left.parent = current_node

        new_root.right = current_node
        current_node.parent = new_root

        if parent:
            """ The node is the root of the AVL tree! """
            if current_node.isLeftChild():
                parent.left = new_root
            else:
                parent.right = new_root
        else:
            self.root = new_root

    def _single_left_rotation(self, current_node):
        """ Handles a left rotation """
        parent = current_node.parent
        new_root = current_node.right

        new_root.parent = current_node.parent
        current_node.right = new_root.left
        if current_node.right:
            current_node.right.parent = current_node
        new_root.left = current_node
        current_node.parent = new_root

        if parent:
            """ The node is the root of the AVL tree! """
            if current_node.isLeftChild():
                parent.left = new_root
            if current_node.isRightChild():
                parent.right = new_root
        else:
            self.root = new_root

    def _double_right_rotation(self, current_node):
        self._single_left_rotation(current_node.left)
        self._single_right_rotation(current_node)

    def _double_left_rotation(self, current_node):
        self._single_right_rotation(current_node.right)
        self._single_left_rotation(current_node)

    def _recalculate_height(self, current_node):
        """ calculate the height of the current_node's subtree """
        if current_node:
            max_height = 0
            left = getattr(current_node, 'left', AVLNode(1))
            right = getattr(current_node, 'right', AVLNode(1))
            max_height = max(left.height, right.height)
            if self.height != max_height:
                current_node.height = max_height
                self._recalculate_height(current_node.parent)



    def __repr__(self):
        return self.nodes;

    def __str__(self, depth=0):
        self.in_order

    def print_structure(self, node, depth=0):
        ret = ""

        # Print right branch
        if self.right != None:
            ret += self.right.__str__(depth + 1)

        # Print own value
        ret += "\n" + ("    "*depth) + str(self.value)

        # Print left branch
        if self.left != None:
            ret += self.left.__str__(depth + 1)

        return ret

    # Traversals

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

    def test_height_successful_on_addition(self):
        """ Ensure Height Is Updated Correctly """
        tree = AVLTree()
        tree.inject(1)
        tree.inject(3)
        self.assertEquals(tree.root.height, 2)

    def test_simple_rotation(self):
        tree = AVLTree()
        injection_list = [1,2,3]
        tree.inject(injection_list)
        self.assertEquals(tree.root.data, 2)

    def test_height_successful_on_list_addition(self):
        """ Ensure Height Is Updated Correctly with a list of options
            Will need to be updated after rebalance is implemented
        """
        injection_list = [3,4,2,51,5,43,1,3214,6]
        tree = AVLTree()
        tree.inject(injection_list)
        self.assertEquals(tree.root.height, 4)
        current_node = tree.root
        print(tree)

        self.assertEquals(tree.root.data, 5)

