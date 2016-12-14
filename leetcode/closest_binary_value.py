"""
Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.

Note:
    Given target value is a floating point.
    You may assume k is always valid, that is: k ≤ total nodes.
    You are guaranteed to have only one unique set of k values in the BST that are closest to the target.

Input:
    Binary Search Tree,
    value k
Output:
    k closest values in a list

Axiums:
    Binary tree is a search Tree
    Binary Tree is not empty
Assumptions:
    Values are ints
    There are at least k+1 values in the tree

Approach:
    Create an inorder(sorted) traversal array
    Then have two pointers, and have one that moves in either direction, picking the closest value then incrementing : Space O(N), Time:(N)
    
"""
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def inorder(self, root, arr=[]):
        if root:
            self.inorder(root.left, arr)
            arr.append(root.val)
            self.inorder(root.right, arr)
            
    
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        arr = []
        self.inorder(root, arr)
        
        ceil = len(arr) - 1
        floor = 0
        mid = 0
        while ceil >= floor:
            mid = (ceil + floor) // 2
            if arr[mid] == target:
                break
            if arr[mid] < target:
                ceil = mid - 1
            else:
                floor = mid + 1
        i,j = mid
        if mid > 0:
            i = i - 1
        else:
            j = j + 1
        # Find closest values
        closestValues = []
        while len(closestValues) < k:
            while i  > 0 and j < len(arr):
                if arr[i] - target < arr[j] - target:
                    closestValues.append(arr[i])
                    i -= 1
            while j < len(arr) and len(closestValues) < k:
                closestValues.append(arr[j])
                j += 1
            while i > 0  and len(closestValues) < k:       
                closestValues.append(arr[i])
                i -= 1
        return closestValues



