""" 1.3 """
from unittest import TestCase

"""
Replace all blank spaces in the string with ‘%20’ without the help of a helper function
BCR: O(N)
Time Complexity O(N)
"""
def urlify(astring):
    alist = list(astring)
    for index, char  in enumerate(alist):
        if char == " ":
            alist[index] = "%20"
    return "".join(alist)


class testUrlify(TestCase):
    """testUrlify for succesful """
    def testSuccesfulJoin(self):
        """ Test for a successful join on urlify """
        stringVal = "blargin flargin"
        expectedResult = "blargin%20flargin"
        result = urlify(stringVal)
        self.assertEqual(result, expectedResult)
