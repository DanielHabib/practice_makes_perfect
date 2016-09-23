import unittest
import random

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None
        self.k = 0
        self.currentK = 0
        self.callCount = 0

    def inorder(self, node, arr=[]):
        if node:
            self.inorder(node.left, arr)
            print (node.value)
            arr.append(node.value)
            self.inorder(node.right, arr)
            return arr

    def preorder(self, node, arr=[]):
        if node:
            print node.value
            arr.append(node.value)
            self.preorder(node.left, arr)
            self.preorder(node.right, arr)

    def postorder(self, node, arr=[]):
        if node:
            self.postorder(node.left, arr)
            self.postorder(node.right, arr)
            print node.value
            arr.append(node.value)

    def addNode(self,node):
        if self.root:
            self.add(self.root, node)
        else:
            self.root = node

    def add(self, current, node):
        if node.value > current.value:
            if not current.right:
                current.right = node
            else:
                self.add(current.right, node)
        else:
            if not current.left:
                current.left = node
            else:
                self.add(current.left, node)

    def find(self, current, value):
        if current:
            if value > current.value:
                return self.find(current.right, value)
            if value < current.value:
                return self.find(current.left, value)
            return True

    def findSmallest(self, current):
        if current:
            if not current.left:
                return current.value
            return self.findSmallest(current.left)

    def findLargest(self, current):
        if current:
            if not current.right:
                return current.value
            return self.findLargest(current.right)

    def findSecondLargest(self, current, parent=None):
        if current:
            if current.right:
                return self.findSecondLargest(current.right, current)
            if not current.left:
                return parent
            return self.findLargest(current.left)

    def findSecondSmallest(self, current, parent=None):
        if current:
            if current.left:
                return self.findSecondSmallest(current.left, current)
            if current.right:
                return self.findSmallest(current.right)
            return parent

    def findKthSmallest(self, currentK=0):
        self.currentK = 0
        self.k = currentK
        val = self._findKthSmallest(self.root)

        if val is None:
            return False

        self.currentK = 0
        # val = self.kthSmallest
        self.kthSmallest = 0
        return val

    def _findKthSmallest(self, current):
        self.callCount += 1
        if current:
            left = self._findKthSmallest(current.left)
            if left:
                return left
            self.currentK += 1
            if self.k == self.currentK:
                return current.value
            right = self._findKthSmallest(current.right)
            if right:
                return right

    def findKthGreatest(self, k):
        currentK = 0
        value = self._findKthGreatest(self.root, currentK, k)
        return value[0]

    def _findKthGreatest(self,currentNode, currentK, k):
        if currentNode:
            nodeValue, currentK = self._findKthGreatest(currentNode.right, currentK, k)
            if not (nodeValue is None):
                return nodeValue, currentK
            currentK += 1
            if currentK == k:
                return currentNode.value, currentK
            return self._findKthGreatest(currentNode.left, currentK, k)
        return None, currentK

    def findSmallestElementGreaterThan(self, value):
        if not self.root:
            return Node(0)
        return self.findVLVGTN(self.root, value)

    def findVLVGTN(self, node, value):
        if not node:
            return None

        # When you are doing binary search, think, under what circumstance would
        # I have to go to the left, and is there any custom processing that needs
        # to be done in that direction. Now think the same for the right
        nextNode = node.right
        if node.value > value:
            nextNode = node.left
        subtreeResult = 0
        subtreeResult = self.findVLVGTN(nextNode, value)
        # print "\nSubtreeResult:{} Node Value:{}".format(subtreeResult, node.value)

        # After I have looked to the side I wanted to look, I will return a result
        # or I will return None
        if subtreeResult > value and node.value <= value:
            return subtreeResult
        if subtreeResult > value and node.value > value:
            return min(node.value, subtreeResult)
        if node.value > value:
            return node.value


class BSTTest(unittest.TestCase):
    def setUp(self):
        self.tree = BST()
        self.values = [7,5,6,3,5,1,2,9,8,15,14]
        for value in self.values:
            self.tree.addNode(Node(value))

    def test_inorder(self):
        """Inorder"""
        inorder = self.tree.inorder(self.tree.root)
        self.assertEquals(inorder, sorted(self.values))

    def test_find_element(self):
        """Able to find element"""
        value = random.choice(self.values)
        exists = self.tree.find(self.tree.root, value)
        self.assertTrue(exists)

    def test_find_nonexistent_element(self):
        """Find Fails Appropriately"""
        value = sum(self.values)
        exists = self.tree.find(self.tree.root, value)
        self.assertFalse(exists)

    def test_find_smallest_element(self):
        """FindSmallest element in the tree"""
        smallestValue = min(self.values)
        valueFound = self.tree.findSmallest(self.tree.root)
        self.assertEqual(smallestValue, valueFound)

    def test_find_largest(self):
        """Test Finding the Largest Value"""
        largestValue = max(self.values)
        valueFound = self.tree.findLargest(self.tree.root)
        self.assertEqual(largestValue, valueFound)

    def test_find_second_largest(self):
        """Find the Second largest"""
        secondLargestValue = sorted(self.values)[-2]
        valueFound = self.tree.findSecondLargest(self.tree.root)
        self.assertEquals(secondLargestValue, valueFound)

    def test_find_second_smallest(self):
        """Find the second smallest value"""
        secondSmallestValue = sorted(self.values)[1]
        valueFound = self.tree.findSecondSmallest(self.tree.root)
        self.assertEquals(secondSmallestValue, valueFound)

    def test_find_kth_smallest(self):
        """Find the kth Smallest Element"""
        sortedValues = sorted(self.values)
        for index, value in enumerate(sortedValues):
            valueFound = self.tree.findKthSmallest(index + 1)
            self.assertEquals(value, valueFound)

    def test_find_kth_smallest(self):
        """Find the kth Smallest Element"""
        sortedValues = sorted(self.values)[::-1]
        for index, value in enumerate(sortedValues):
            valueFound = self.tree.findKthGreatest(index + 1)
            self.assertEquals(value, valueFound)

    def test_find_smallest_element_greater_than(self):
        """Find the smallest element greater than another element"""
        valToFind = max(self.values)

        valueFound = self.tree.findSmallestElementGreaterThan(valToFind)
        self.assertEquals(None, valueFound)

    def test_find_smallest_element_greater_than_highest_returns_none(self):
        """Find the None when searching for an element greater than the greatest element"""
        valToFind = 5

        valueFound = self.tree.findSmallestElementGreaterThan(valToFind)
        self.assertEquals(6, valueFound)
