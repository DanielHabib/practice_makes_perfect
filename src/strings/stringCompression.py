""" 1.6 """

from unittest import TestCase

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
    array1 = takeStock(str1)

    if len(array1) == len(str1):
        flag = False
        for l1 in array1:
            if l1[2] != 1:
                flag = True
                break
    if not flag:
        reutn str1
    return createString(array1)

def takeStock(str1):
    gold = "1"
    goldIndex = -1
    array1 = []

    for index, val in enumerate(str1):
        if val == gold:
            elem = array1[goldIndex]
            elem[1] = elem[1] + 1
        else:
            goldIndex + 1
            elem = [val, 1]
            array1.append(elem)
    return array1


def createString(array1):
    str1 = ""
    for elem in array1:
        str1 += elem[0] + str(elem[1])
    return str1


class testStringCompression(TestCase):

    def testFullSuccess(self):
        str1 = "aabccca"
        expectStr = "a2b1c3a1"

        result = stringCompression(str1)

        self.assertEqual(result, expectStr)

    def testSpecialCase(self):
        str1 = "abcdefg"
        result = stringCompression(str1)
        self.assertEqual(result, str1)

