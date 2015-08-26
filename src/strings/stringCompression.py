""" 1.6 """

"""
    Time: 12:59
    Problem: given 'aabccca' return 'a2b1c3a1', if the string is unchanged,
            return the original string

    BCR: O(N)
"""

def stringCompression(str1):
    """
        Time Complexity: O(N)
        Space Complexity:  

        Steps:
            1: Take Stock
            1.5: Check for unphased string
            2: Create string
    """


def takeStock(str1):
    gold = "1"
    goldIndex = -1
    array1 = []

    for index, val in enumerate str1:
        if val == gold:
            elem = array1[goldIndex]
            elem[1] = elem[1] + 1
        else:
            goldIndex + 1
            elem = [val, 1]
            array1[goldIndex] = elem
