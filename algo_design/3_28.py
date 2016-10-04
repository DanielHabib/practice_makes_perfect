'''
Given an unordered array X create an array M where Mi = Xo...Xi-1 * Xi+1...Xn
'''
def specialized_product_array(n):
    m = [None] * len(n)
    for i, value in enumerate(n):
        m[i] = value
        if i > 0: m[i] *= m[i - 1]
    trailing_product_so_far = 1
    j = len(n) - 1
    while j >= 0:
        m[j] = trailing_product_so_far
        if j > 0: m[j] *= m[j - 1]
        trailing_product_so_far *= n[j]
        j -= 1
    return m

import unittest

class Test(unittest.TestCase):
    def test_specialized_product_array(self):
        n = [6, 3, 5]
        m = specialized_product_array(n)
        self.assertEquals(m, [15, 30, 18])
    def test_empty_array(self):
        n = []
        m = specialized_product_array(n)
        self.assertEquals(m, [])
