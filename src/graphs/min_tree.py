""" 4.2 Min Tree """

def mintree(arr):
    """
        BCR: O(N)
        Time Complexity: O(N)
        Space Complexity: I still don't fully understand the SC
    """
    mid = len(arr)//2
    tree = BinaryTree()
    tree.root = arr[mid]
    mintree_helper(arr, tree.root)


def mintree_helper(arr, node):
    if len(arr) // 2:
        mid = len(arr)//2
        left = arr[: mid]
        right = arr[mid:]

        node.leftchild = mintree_helper(arr, arr[mid-mid//2])
        node.rightchild = mintree_helper(arr, arr[mid+mid//2])

        return arr[mid]
