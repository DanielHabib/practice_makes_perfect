""" Problem 1.2 """
"""
    Problem:
        Determine if two strings are permutations of each other
"""
def isPermuation(string1, string2):
    """
        SC:
        TC:

    """
    if len(string1) != len(string2):
        return False
    valDict = {}
    for val in string1:
        try:
            valDict[val] = valDict[val] + 1
        except:
            valDict[val] = 0
    for val in string2:
        try:
            if valDict[val] == 0:
                return False
            else:
                valDict[valDict] = valDict[val] - 1

        except:
            return False
    return True
