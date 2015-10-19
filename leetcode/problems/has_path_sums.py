# Definition for a binary tree node.
# class TreeNo
≈ççde(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        
    NOTES: Simple tree traversal, were we pass down the sum up till this point.
           if the correct sum is found on the condition that it is a leaf, then return True!
        """
        
    def calc_sums(self, node, sum, sum_expected):
        if node:
            sum = sum + node.val
            if not node.left and not node.right:
                if sum = sum_expected:
                    return True
                else:
                    return False
            el
