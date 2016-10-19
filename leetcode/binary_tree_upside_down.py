'''
Q: Given a binary Tree where all the right nodes are either leaf nodes are with 
a sibling or empty, flip it upside down and turn it into a tree 
where the original right nodes turned into left leaf nodes. Return the new root


     1
    / \
   2   3
  / \
 4   5
    *******
*** Becomes ***
    *******
      4
     / \
    5   2
       / \
      3   1

Axiums: The order is important
Assumptions: All values are integers. 

Notes:
    the left node becomes the subtree root
    the current node becomes the right child
    the right node becomes the left child

Approach:
    Traverse Left and build the new tree out of the current tree

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
  	newRoot = None
        if not root or not root.left:
            return root

        left = root.left
        nextHead = left.left
        left.left = root.right
        left.right = root
        root.left, root.right = None, None 
        
        return self.flip(nextHead, left)
            
            

    def flip(self, node, right):
        if node:
            newLeft = node.right
            node.right = right
            
            
   





                
