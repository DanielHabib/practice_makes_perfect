class MissingNodeError(Exception):
    """The node you are looking for is not available"""


class TreeNode:
    """A Node in a Basic Tree Datastructure"""
    def __init__(self, val, children=None):
        """
            args:
                val: payload of the node
                children: children of the current node
        """
        self.val = val
        self._children = children

    @property
    def children(self):
        return self._children

    @setter.children
    def children(self, children):
        self._children = children

    def add_child(self, node):
        """
            args:
                node, A Tree Node to append to _children
        """
        assert isinstance(node, TreeNode)
        self.children.append(node)

    def remove_child(self, node):
        """
            args:
                node, A TreeNode the is in self.children.append
            return:
                None
            raises:
                 MissingNodeError, if the node you are looking to delete
                    is not a child of the current node
        """
        if node in self.children:
            self.children.remove(node)
        else:
            raise MissingNodeError


class Tree:
    """Tree Datastructure
    For storing data in a tree hierarchy where each node has children

    In order to maintain a list of all nodes in the tree,
    all additions must go through the tree, or the node needs to have some
    relationship to the tree. I dont think this is truly neccesary so I wont
    include it
    """
    def __init__(self, root=None):
        """
            args:
                root, TreeNode that is set as the root value
        """
        assert isinstance(root, TreeNode)
        self.root = root
