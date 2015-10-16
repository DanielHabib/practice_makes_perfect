class BST:
    def __init__(self, root=None):
        self.root = root


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


class Node:
    def __init__(self, val, leftchild=None, rightchild=None):
        self.val = val
        self.leftchild = leftchild
        self.rightchild = rightchild
