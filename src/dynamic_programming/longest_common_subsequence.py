"""
Longest common subsequence between two arrays
"""
from unittest import TestCase
from collections import defaultdict
import time

class LCSS:
    def __init__(self):
        self.memo = defaultdict(dict)
    def lcssLength(self,a, b):
        if len(a) in self.memo and len(b) in self.memo[len(a)]: return self.memo[len(a)][len(b)]

        if a == [] or b == []: return 0
    
        maxLength = self.lcssLength(a[:-1], b[:-1])
        if a[-1] == b[-1]:
            maxLength += 1

        maxLength = max(maxLength, self.lcssLength(a[: -1], b))
        maxLength = max(maxLength, self.lcssLength(a, b[: -1]))
        self.memo[len(a)][len(b)] = maxLength
        return maxLength
    
    def lcss(self, a, b):
        if len(a) in self.memo and len(b) in self.memo[len(a)]: return self.memo[len(a)][len(b)]
        print("Enter:", a, b)
        if a == [] or b == []: return []
        
        lcss = self.lcss(a[:-1], b[:-1])

        if a[-1] == b[-1]: 
            print(lcss, a[-1], a, b)
            lcss.append(a[-1])

        lcssA = self.lcss(a[:-1], b)
        if len(lcssA) > len(lcss): lcss = lcssA

        lcssB = self.lcss(a, b[:-1])
        if len(lcssB) > len(lcss): lcss = lcssB

        self.memo[len(a)][len(b)] = lcss # Currently my memo is way to big. Storing whole arrays instead of recreating them via a path is extremely inefficient.
        return lcss

class TestLcss(TestCase):
    def test_lcss(self):
        a = [1,2,4]
        b = [1,3,4]
        answer = [1, 4]
        lcss = LCSS()
        self.assertEquals(lcss.lcss(a, b), answer)

    def test_lcss_2(self):
        a = [2,4,4]
        b = [1,2,4]
        answer = [2, 4]
        lcss = LCSS()
        self.assertEquals(lcss.lcss(a, b), answer)

    def test_lcss_different_length(self):
        a = [1,2,4]
        b = [1,3,4,5,6]
        answer = [1,4]
        lcss = LCSS()
        self.assertEquals(lcss.lcss(a, b), answer)

    def test_lcss_long(self):
        a = [1,2,4,2,5,62,6,2,7,8,9,3,4,6,7,8]
        b = [1,3,4,5,6,1,4,51,15,152,62,8,9,3,7,8]
        answer = [1,8]
        start = time.time()
        lcss = LCSS()
        #self.assertEquals(lcss.lcss(a, b), answer)
        end = time.time()
        self.assertTrue(end-start < 2)



class TestLcssLength(TestCase):

    def test_lcss(self):
        a = [1,2,4]
        b = [1,3,4]
        answer = 2
        lcss = LCSS()
        self.assertEquals(lcss.lcssLength(a, b), answer)

    def test_lcss_different_length(self):
        a = [1,2,4]
        b = [1,3,4,5,6]
        answer = 2
        lcss = LCSS()
        self.assertEquals(lcss.lcssLength(a, b), answer)

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
        lcss = LCSS()
        self.assertEquals(lcss.lcssLength(a, b), answer)
        end = time.time()
        self.assertTrue(end-start < 2)
