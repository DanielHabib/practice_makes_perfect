"""
Longest common subsequence between two arrays
"""
from unittest import TestCase
from collections import defaultdict
import time

memo = defaultdict(dict)

def lcssLength(a, b):
    if len(a) in memo and len(b) in memo[len(a)]: return memo[len(a)][len(b)]

    if a == [] or b == []: return 0
    
    maxLength = lcssLength(a[:-1], b[:-1])
    if a[-1] == b[-1]:
        maxLength += 1

    maxLength = max(maxLength, lcssLength(a[: -1], b))
    maxLength = max(maxLength, lcssLength(a, b[: -1]))
    memo[len(a)][len(b)] = maxLength
    return maxLength


class TestLcss(TestCase):

    def test_lcss(self):
        a = [1,2,4]
        b = [1,3,4]
        answer = 2
        self.assertEquals(lcssLength(a, b), answer)

    def test_lcss_different_length(self):
        a = [1,2,4]
        b = [1,3,4,5,6]
        answer = 2
        self.assertEquals(lcssLength(a, b), answer)



    def test_lcss_large_input(self):
        # Tried running this without the memo,, currently at 3 minutes of pure computation. It will be pretty cool to see what happens after a cache (memo) is implemented
        # If it makes it to 5 minutes I'm calling it
        # Based off my time complexity analysis, w/o a cache this algo should take at LEAST 4.5 million operations to complete....... I'm pretty sure this would take a couple hours to complete. Kind of makes this algorithm useless
        # Officially hit 5 minutes and 45 seconds of execution, I'm calling it. Time to implement the cache
        # ******* After adding cache this script finishes in under a second.***** Incredible
        a = [1,2,4,2,5,62,6,2,7,8,9,3,4,6,7,8]
        b = [1,3,4,5,6,1,4,51,15,152,62,8,9,3,7,8]
        answer = 9
        start = time.time()
        self.assertEquals(lcssLength(a, b), answer)
        end = time.time()
        self.assertTrue(end-start < 10)
