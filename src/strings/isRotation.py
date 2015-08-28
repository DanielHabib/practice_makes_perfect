""" 1.9 """
from unittest import TestCase

"""
    Time: 22:21
    BCR:O(N)
    Time Complexity: The time of subString
    Space Complexity: O(N)

    Problem: find is s2 is a rotation of s1, using the function `subString`
        once
"""


def is_substring(smallstring, bigstring):
    """ Calculates
    whether smallString is a substring of bigString """
    return smallstring in bigstring


def is_rotation(s1, s2):
    """
        Assumptions:
    """
    if len(s1) != len(s2):
        return False
    s3 = s2 + s2

    if is_substring(s1, s3):
        return True
    return False


class TestIsRotation(TestCase):

    def testSuccessfulRotation(self):
        """ Test Succesful rotation """
        s1 = "abcdef"
        s2 = "feabc"

        self.assertTrue(is_rotation(s1, s2))

    def testFailureRotation(self):
        """ Test Failure situation """
        s1 = "abcdefds"
        s2 = "feabc"

        self.assertFalse(is_rotation(s1, s2))
