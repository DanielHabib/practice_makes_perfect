'''
Confirm two binary Trees are identical
'''
import unittest
import random


class Node:
    def __init__(self, value, left=None, right=None):
        self.__dict__.update({x:k for x, k in locals().items() if x != 'self'})

def createTree():
    a = 0
    b = 100
    n = 200
    current = Node(random.randint(a, b))
    head = current
    for i in range(n):
        newLeftNode = Node(random.randint(a, b))
        newRightNode = Node(random.randint(a, b))
        current.left = newLeftNode
        current.right = newRightNode
        current = [current.left, current.right][random.randint(0, 1)]
    return head

def inorder(node, arr=None):
    if arr is None:
        arr = []
    if node:
        inorder(node.left, arr)
        arr.append(node.value)
        inorder(node.right, arr)
        return arr


def checkIdentical(head1, head2):
    if bool(head1) ^ bool(head2):
        return False
    if not head1:
        return True
    if head1.value != head2.value:
        return False
    return checkIdentical(head1.left, head2.left) and checkIdentical(head1.right, head2.right)

if __name__ == '__main__':
    head = createTree()
    print(len(inorder(head)))


class TestNode(unittest.TestCase):

    def test_checkIdentical(self):
        '''
        Confirm two binary Trees are identical
        '''
        head = createTree()
        self.assertTrue(checkIdentical(head, head))

    def test_checkNotIdentical(self):
        '''
        Confirm two binary Trees are not identical
        '''
        head = createTree()
        head2 = createTree()
        self.assertFalse(checkIdentical(head, head2))
