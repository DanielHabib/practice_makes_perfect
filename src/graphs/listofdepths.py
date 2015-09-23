""" List Of Depths """

def lod(btree):
    lldict = dict()
    lod_help(btree.root, lldict, 0)

def lod_help(node, lldict, height):
    height = height + 1
    try:
        ll = lldict[depth]
        ll.append(node.val)
    except, KeyError:
        ll = LinkedList(node.val)
        lldict[depth] = ll
    lod_help(node.leftChild, lldict, height)
    lod_help(node.rightChild, lldict, height)
