def validate(bst):
    validate_helper(bst.root, None, None)

def validate_helper(node, min, max):
    if node.leftChild:
        if node.leftChild.val >= node.val or node.leftChild.val < min:
            return False
    if node.rightChild:
        if node.rightChild.val < node.val or node.rightChild.val > max:
            return False

    if validate_helper(node.leftChild, min, node.val) and\
         validate_helper(node.leftChild, min, node.val):
        return True
    else:
        return False
