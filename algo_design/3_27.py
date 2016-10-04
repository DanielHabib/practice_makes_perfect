'''
Find the starting point of the loop in the linked list
'''
import unittest
import random

def findloopstart(head):
    slow = head
    fast = head
    if head is None: return None

    while fast:
        if not fast.next or not fast.next.next:
            return False
        fast = fast.next.next
        slow = slow.next
        if fast.value == slow.value:
            break
    start = head
    while start.value != fast.value:
        print('Start:{0} Fast:{1}'.format(start, fast))
        start = start.next
        fast = fast.next
    return start

class Node:
    def __init__(self, value=None, next=None):
        self.__dict__.update({x:k for x, k in locals().items() if x != 'self'})

def createLoopedLinkedList(middlePosition=10):
    x = 0
    middle, prev, head = None, None, None
    if middlePosition > 30:
        raise Exception("Educate yo self fool")
    for x in range(random.randint(20, 30)):
        current = Node(x)
        if not head: head = current
        if prev: prev.next = current
        prev = current
        if x == middlePosition:
            middle = current
    current.next = middle
    return head

class TestLinkedList(unittest.TestCase):
    def test_find_loop_start(self):
        head = createLoopedLinkedList(middlePosition=10)
        self.assertEquals(findloopstart(head).value, 10)
