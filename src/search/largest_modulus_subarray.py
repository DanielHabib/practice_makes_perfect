class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BST:
    def __init__(self)
        self.root = None


def max_subarray_modulus(n, m):
    # Start Creating Prefix Array
    # # The prefix array will contain the (total mod m)
    # Also put those values into a binary tree for search after
    # We will look for the next largest aiming for `-1`.
    # # Why `-1`? Because the modulus of `-1` is always the highest possible modulus, so the moduluss 7 and 6, 7-6 = 1 but 6-7 resolves to -1 + M which is 8 will give us 7, 7 (Congruent) -1 which means the modulus is the same to both
    # This will give us O(Nlog(N))

    prefixArr = [0] * n
    prefixTree = BST()
    currTotal = 0
    highestModulus = 0
    for index, value in enumerate(n):
        currTotal += value
        currentMod = currTotal % m
        prefixArr[index] = currentMod
        highestModulus = max(highestModulus, prefixTree.findNextGreatest(currentMod))
        prefixTree.add(currMod)
        if highestModulus == (m - 1):
            return highestModulus
    return highestModulus

