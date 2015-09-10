""" 2.3 Delete the middle node given only access to that node """

def del_middle(node):
    """
    BCR: O(N)
    time: 5:52
    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    if not node.next:
        node = None
        return
    node = node.next
    del_middle(node.next)
