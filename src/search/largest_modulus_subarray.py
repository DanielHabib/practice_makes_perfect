class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None
        
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print (node.value)
            self.inorder(node.right)
                
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
    
    def findNextGreatest(self, value):
        if self.root:
            if self.root.value >= value:
                return self.findLessThan(self.root.left, value, self.root)
            else:
                return self.findGreaterThan(self.root.right, value, self.root)

        return Node(0)
        
    def find(self, current, value, parent=None):
        if current.value > value:
                       
            
    def findLessThan(self, current, value, parent=None):
        
    def findGreaterThan(self, current, value, parent=None):
        if current.value < value:
            return self.findGreaterThan(current.right, value, current)
        rightMost = self.findRightMostLessThan(current.left, value, current)
        if rightMost:
            return rightMost
        return parent

    def findRightMostLessThan(self, current, value, parent=None):	

def max_subarray_modulus(n, m):
    # Start Creating Prefix Array
    # # The prefix array will contain the (total mod m)
    # Also put those values into a binary tree for search after
    # We will look for the next largest aiming for `-1`.
    # # Why `-1`? Because the modulus of `-1` is always the highest possible modulus, so the moduluss 7 and 6, 7-6 = 1 but 6-7 resolves to -1 + M which is 8 will give us 7, 7 (Congruent) -1 which means the modulus is the same to both
    # This will give us O(Nlog(N))

    prefixTree = BST()
    currTotal = 0
    highestModulus = 0
    for index, value in enumerate(n):
        currTotal += value
        currentMod = (currTotal % m)
        #print ('Current Mod: {}'.format(currentMod))
        next_greatest_so_far = prefixTree.findNextGreatest(currentMod).value
        max_sub_so_far = (currentMod - next_greatest_so_far) %m

        print "\nCurrent Value: {0}\n Total So Far: {1}\n Current Modulus:{2}\n Next Greatest From Prefix Tree {3}\n highest_modulus_so_far:{4}".format(value,currTotal, currentMod, next_greatest_so_far, highestModulus)
        highestModulus = max(highestModulus, max_sub_so_far, currentMod)
        prefixTree.addNode(Node(currentMod))
        if highestModulus == (m - 1):
            break
    print highestModulus
#   prefixTree.inorder(prefixTree.root)

    
cases = int(input())
for case in range(cases):
    length, modulus = [int(x) for x in input().split(' ')]
    arr = [int(x) for x in input().split(' ')]
    max_subarray_modulus(arr, modulus)

    
    
