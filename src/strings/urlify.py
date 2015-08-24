""" 1.3 """
from unittest import TestCase
 
"""
Replace all blank spaces in the string with ‘%20’ without the help of a helper function

Notes:
Solve this problem in place without the use of additional data structures
BCR:
Time Complexity O(N)
"""
def urlify(astring):
    alist = list(astring)
    for index, char  in alist.iteritems():
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

        self.assertEqual(stringVal, expectedResult)

