""" 2.5 Sum Lists """
"""
    Sum Two lists who's values are digits in reverse order
"""

def sum_lists(a, b):
    """
        Assumptions: Values are ints, singly and doubly don't matter, assume
                singly
        mistakes: When you see things in reverse order through LL problems,
            They can usually be solved via recursion

    """
    aS = ""
    bS = ""
    current = a.head
    while current:
        aS = str(current.data) + aS
        current = current.next
    current = b.head
    while current:
        bS = str(current.data) + bS
    return int(aS) + int(bS)
