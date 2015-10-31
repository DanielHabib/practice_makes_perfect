# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        
        NOTES: First we need to find whether the floating point is closer to the bottom or the top. Maybe there is a math.round 
                function available?
                Secondly we need to traverse the binary search tree until we find where the nodes value exists or when we find that the node lies somewhere between the parent and its child.
                
        STEPS:
            1. Set up basic tree traversal
            2. Add in checks to see whether the value is the current value, or lies between the current value and one of its children
        
            3. Handle leaf cases appropriately
        
        EDGE CASES: Keep forgetting to handle the edge cases
        """
        
        closest = [sys.maxint, None]
        self.search(root, target, closest)
        return closest[1]
        
    def search(self, node, target, closest):
        if node:
            if node.val == target:
                closest[0] = 0
                closest[1] = node.val
                return
            
            if node.val > target:
                diff = abs(node.val-target) 
                if diff < closest[0]:
                    closest[0] = diff
                    closest[1] = node.val
                self.search(node.left, target, closest)
            if node.val < target:
                diff = abs(node.val-target) 
                if diff < closest[0]:
                    closest[0] = diff
                    closest[1] = node.val
                self.search(node.right, target, closest)
        
        
