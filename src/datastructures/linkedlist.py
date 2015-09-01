""" Linked List Practice """

from unittest import TestCase

class OccupiedNodeError(Exception):
    """ The next node is occupied and cannot be added """

class LinkedList:
    """ Allows for Nodes to not worry about the head value and allows all
     external references to simply point to the head property of the linked
     list
    """
    def __init__(self, head):
        self.head = head


class Node:
    """ Singly Linked List Node """
    def __init__(self, data, nextNode=None):
        self.data = data
        self.next = nextNode

    def addNode(self, data):
        if type(data) != type(self):
            nextNode = Node(data)
        else:
            nextNode = data

        if not self.next:
            self.next = nextNode
        else:
            raise OccupiedNodeError(
                'The data value {0} cannot be added because the next node'\
                'already exists'.format(data))


class TestLinkedLists(TestCase):
    """ Test both the linked list and node classes """

    def testAddNodeSuccessfully(self):
        node1 = Node(1)
        node2 = Node(2)
        node1.addNode(node2)
        self.assertEquals(node1.next, node2)

    def testAddDataSuccessfully(self):
        node1 = Node(1)
        nodeTwoData = 2
        node1.addNode(nodeTwoData)
        self.assertEquals(node1.next.data, nodeTwoData)

    def testExceptionIsRaised(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node1.addNode(node2)
        with self.assertRaises(OccupiedNodeError):
            node1.addNode(node3)
