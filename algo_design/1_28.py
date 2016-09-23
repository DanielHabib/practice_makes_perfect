"""
Integer Division
"""
def intDivision(n, k):
    c = 0

    if k == 0:
        return False

    while n > k:
        n = n - k
        c += 1

    return c

import unittest
class TestIntDivision(unittest.TestCase):
    def test_int_division(self):
        result = intDivision(5, 2)
        self.assertEquals(result, 2)
    def test_int_division_with_zero(self):
        result = intDivision(5, 0)
        self.assertEquals(result, False)
    def test_returns_zero_if_k_big(self):
        result = intDivision(0, 2)
        self.assertEquals(result, 0)

