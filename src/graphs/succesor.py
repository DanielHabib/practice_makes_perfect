""" 4.6 Succesor """

def check_next(node):
    if node.rightChild:
        return traverseLeft(node.rightChild)
    elif node.parent.leftChild == node:
        return node.parent
    elif node.parent.rightChild == node:
        return traverseParent(node.parent)

def traverseLeft(node):
    if not node.leftChild:
        return node
    return traverseLeft(node.leftChild)

def traverseParent(node):
    if node.parent.leftChild == node:
        return node.parent
    elif node.parent == None:
        return None
    return traverseParent(node.parent)
