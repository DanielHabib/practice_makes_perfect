""" 2.2  Return The Kth Element in a SINGLY linked list """

from datastructures.linkedlist import LinkedList, Node
from unittest import TestCase
"""
    BCR:O(N)
    Steps:
        1. Loop through the linked list and count the length
        2. Second loop through and only get to the N-1-k element

"""

def returnKth(k, linkedlist):
    """
        Time Complexity: O(N)
        Space Complexity: O(1)

    """
    if not linkedlist.head:
        return False

    head = linkedlist.head
    node = linkedlist.head
    counter = 1
    while node.next:
        counter += 1
        node = node.next
    i = 1
    node = head
    while i < counter-k:
        i = i + 1
        node = node.next
    return node


class TestReturnKth(TestCase):

    def testReturnKth(self):
        """ Test Successful return Kth """
        k = 2
        linkedlist = LinkedList()

        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        linkedlist.head = node1
        node1.addNode(node2)
        node2.addNode(node3)
        node3.addNode(node4)
        result = returnKth(k, linkedlist)
        self.assertEquals(node2, result)
