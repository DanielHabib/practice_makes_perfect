class InvalidHeightError(Exception):
    """The Given Height Is Invalid"""
class AVLNode:
    def __init__(self, val, left=None, right=None, parent=None, height=1):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
        self.height = height

    def bfactor(self):
        left = getattr(self.left, 'height', 0)
        right = getattr(self.right, 'height', 0)
        return left - right

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, node):
        if node is not None:
            assert isinstance(node, AVLNode)
            self._left = node
        else:
            self._left = None

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, node):
        if node is not None:
            assert isinstance(node, AVLNode)
            self._right = node
        else:
            self._right = None

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, new_height):
        assert isinstance(new_height, int)
        if height >= 1:
            self._height = new_height
        else:
            raise InvalidHeightError


class AVLTree:
    __slots__ = ["root"]
    def __init__(self, root):
        self.root = root

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, node):
        if node is not None:
            assert isinstance(node, AVLNode)
            self._root = node
        else:
            self._root = None

    def add(self, node):
    """The only difference is the rebalancing"""
        assert isinstance(node, AVLNode)
        if not self.root:
            self.root = node
        self._add(self.root, node)
        self._rebalance(node)

    def _add(self, current, node):
        """Handles the recursion of AVL Tree addition
           Same as BInary Tree 
       """
        if node.val == current.val:
            raise DuplicateNodeError
        if node.val < current.val:
            if not current.left:
                current.left = node
                node.parent = current
                if node.height + 1 > current.height:
                    current.height= node.height + 1
            else:
                self._add(current.left, node)
        elif node.val > current.val:
            if not current.right:
                current.right = node
                node.parent = current
            else:
                self._add(current.right, node)

        def _rebalance(self, node):
            if node:
                if node.parent:
                    prev_parent_bf = node.parent.bfactor()
                if node.bfactor() < -1:
                    self.right_rotation(node)
                elif node.bfactor() > 1:
                    self.left_rotation(node)
                left = getattr(node, 'left', 0)
                right = getattr(node, 'right', 0)
                height = max(left, right) + 1

                if node.parent:
                    if prev_parent_bf != node.parent.bfactor():
                        self._rebalance(node)

        def right_rotation(self, node):
            if node.left.bfactor() > 0:
                self._single_left(node.left)
                self._single_right(node)
            else:
                self._single_right(node)

        def left_rotation(self, node):
            if node.right.bfactor() < 0:
                self._single_right(node.right)
                self._single_left(node)
            else:
                self._single_left(node)

        def _single_right(self, node):
            new_root = node.left
            parent = node.parent
            # Child Swap
            node.left, new_root.right = new_root.right, node
            # Be sure all children have their parents changed correctly
            node.left.parent = node
            node.parent = new_root
            # Parent Swap
            if parent:
                new_root.parent = parent
                if node == parent.left:
                    parent.left = new_root
                elif node == parent.right:
                    parent.right = new_root

        def _single_left(self, node):
            new_root = node.right
            parent = node.parent
            #Handle Sub Tree
            node.right, new_root.left = new_root.left, node
            node.right.parent, node.parent = node, new_root
           # Attach to larger tree
            if parent:
                new_root.parent = parent
                if node == parent.right:
                    parent.right = new_root
                elif node == parent.left:
                    parent.left = new_root

