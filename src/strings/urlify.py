""" 1.3 """
"""
Replace all blank spaces in a string with %20
"""


def urlify(stringVal):
    """
        Time Complexity:
        Space Complexity:
    """
    alist = list(stringVal)
    for index, val in alist.iteritems():
        if val == " ":
            alist[index] = "%20"
    return "".join(alist)
