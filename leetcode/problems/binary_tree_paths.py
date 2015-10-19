# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# NOTES: This requires tree traversal, where we pass in the path to current node, and append to the result list
#        As we continue on
# BCR: O(N)
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """

      paths = []
      self.binary_tree_helper(root, "", paths) 
      return paths

    def binary_tree_helper(self, node, current_path, paths):
        if node:
            if current_path == "":
                current_path = str(node.data)
            else:
                current_path += "->" + str(node.data)
            if not node.right and not node.left:
                paths.append(current_path)
            else:
                self.binary_tree_helper(node.left, current_path, paths)
                self.binary_tree_helper(node.right, current_path, paths)

