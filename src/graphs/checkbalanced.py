""" 4.4 Check Balanced """


def check_balanced(btree):
    return check_balanced_helper(btree.root, {}, 0)


def check_balanced_helper(node, depthDict, height):
    height = height + 1
    if not node:
        return True
    if not node.leftChild and not node.rightChild:
        depthDict[height] = node
        if len(depthDict.keys) > 2:
            return False
        elif len(depthDict.keys) == 2:
            a = depthDict.keys[0]
            b = depthDict.keys[1]
            if abs(a-b) > 1:
                return False
    if check_balanced_helper(node.leftChild, depthDict, height) and \
        check_balanced_helper(node.rightChild, depthDict, height):
        return True
    else:
        return False
""" Book solution is different
online soln: pseudo code:
IsHeightBalanced(tree)
    return (tree is empty) or
           (IsHeightBalanced(tree.left) and
            IsHeightBalanced(tree.right) and
            abs(Height(tree.left) - Height(tree.right)) <= 1)

"""
