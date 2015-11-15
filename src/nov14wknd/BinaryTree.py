class DuplicateNodeError(Exception):
    """A collision has occured and this node cannot be added to the tree"""

class NodeNotFound(Exception):
    """Coulddt find the node"""

class BinaryTreeNode:
    """BinaryTreeNode for supporting BinaryTree"""
    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, node):
        if node is not None:
            assert isinstance(node, BinaryTreeNode)
            self.parent = node
        else:
            self.parent = None

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, node):
        if node:
            assert isinstance(BinaryTreeNode, node)
            self.left = node
        else:
            self.left = None

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, node):
        if node:
            assert isinstance(BinaryTreeNode, node)
            self.right = node
        else:
            self.right = None

    def hasChildren(self):
        return not self.left and not self.right

    def isLeftChild(self):
        if node.parent and node.parent.left == self:
            return True
        return False

    def isRightChild(self):
        if node.parent and node.parent.right == self:
            return True
        return False

class BinaryTree:
    """BinaryTree DataStructure"""
    def __init__(self, root):
        self.root = root

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, node):
        assert isinstance(node, BinaryTreeNode)
        self.root = node


class BinarySearchTree(BinaryTree):
    """BinarySearchTree DataStructure"""

    def __init__(self, root):
        super().__init__(root)

    def add_node(self, node):
        """Add a node to the binary search tree

            args:
                node, BinaryTreeNode that is going to be added to the
                search tree
            raise: Duplicate Node error
            stats:
                time: Best O(log(N)) | Worst: O(N)
                space: Best O(log(N)) | Worst: O(N), it depends on the depth of
                        the recursion
        """
        if not self.root:
            self.root = node
        self.add_node(root, node)

    def _addition_helper(self, current, node):
        """Handles the recursion aspect of addition

            args:
                current(BinaryTreeNode), the current node in our recursion, this is the node
                that we are currently at in the tree, we use this to determine
                what direction to progress in
                node(BinaryTreeNode), the node ot be added

            return:
                 None, strictly used to exit the recursion here
        """
        if current.val == node.val:
            raise DuplicateNodeError
        if node.val < current.val:
            if not current.left:
                current.left = node
                node.parent = current
                return True
            return _addition_helper(current.left, node)
        else:
            if not current.right:
                current.right = node
                node.parent = current
                return True
            return _addition_helper(current.right, node)

    def find(self, val):
        """ Find Based off of the value

            args:
                val, find the node with the same value

            stats:
                time: Best O(log(N)) | Worst: O(N)
                space: Best O(log(N)) | Worst: O(N), it depends on the depth of
                        the recursion
        """
        if not self.root:
            return False
        self._find(self.root, val)

    def _find(self, current, val):
        """Handles the recursion of finding the value
            stats:
                time: Best O(log(N)) | Worst: O(N)
                space: Best O(log(N)) | Worst: O(N), it depends on the depth of
                        the recursion
        """
        if not current:
            return False
        if current.val == val:
            return True
        if val < current.val:
            return self._find(current.left, val)
        if val > current.val:
            return self._find(current.right, val)

    def delete(self, val):
        """Delete The Node with the Value"""
        self._find_delete(self.root, val)

    def _find_delete(self, current, val):
        if current:
            if current.val == val:
                return self._remove(current)
            if val < current.val:
                return self._find_delete(current.left, val)
            if val > current.val:
                return self._find_delete(current.right, val)

        raise NodeNotFound

    def _remove(self, node):
        """Remove the Node This is

            args:
                node, the node to be removed
        """
        parent = node.parent
        left = node.left
        right = node.right
        if not node.hasChildren:
            if isLeftChild:
                parent.left = None
            elif isRightChild:
                parent.right = None
        if bool(node.left) != bool(node.right):
            if node.left:
                if node.isLeftChild():
                    parent.left = node.left
                elif node.isRightChild():
                    parent.right = node.left
            elif node.right:
                if node.isRightChild():
                    parent.right = node.right
                elif node.isLeftChild():
                    parent.left = node.right
        if node.left and node.right:
            replacement = self._find_smallest_of_subtree(node.right)
            replacement.parent.left = None
            parent.left = replacement
            if node.isLeftChild():
                replacement.left = node.left
                replacement.right = node.right

    def _find_smallest_of_subtree(self, current):
        if current.left:
            return self._smallest_node(current.left)
