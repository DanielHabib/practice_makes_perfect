""" Problem 1.2 """
from unittest import TestCase

"""
    Problem:
        Determine if two strings are permutations of each other
"""
def isPermuation(string1, string2):
    """
        Time Complexity: O(N), N being the length of either string, since if they aren't
            equal then it is constant time
        Space Complexity: O(N)
        Alt Soln :
            It would be possible to to sort both strings since this would
            make their values line up perfectly if they were permutations of
            each other. Downside to that is the sort would run in O(Nlog(N)).
            This would be the solution without additional datastructures.
            Space Complexity would be constant.

    """
    if len(string1) != len(string2):
        return False

    valDict = {}
    for val in string1:
        try:
            valDict[val] = valDict[val] + 1
        except:
            valDict[val] = 1
    for val in string2:
        try:
            if valDict[val] == 0:
                return False
            else:
                valDict[val] = valDict[val] - 1
        except:
            return False
    return True


class isPermutationTest(TestCase):
    def testSuccesfulPermutation(self):
        string1 = "asdfghjkl"
        string2 = "lkjhgfdsa"
        assert isPermuation(string1, string2)

    def testNonPermutation(self):
        string1 = "asdfghjkl"
        string2 = "lkjhgpdsa"
        assert not isPermuation(string1, string2)
