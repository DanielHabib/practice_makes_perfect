"""
O(N) Fib
"""
from unittest import TestCase

def fib(n):
    return fib_help(n, {})
def fib_help(n, memo):
    if memo.get(n, False):
        return memo[n]

    if n == 0 or n == 1:
        return n

    val1 = fib_help(n - 1, memo)
    val2 = fib_help(n - 2, memo)

    memo[n] = val1 + val2
    return memo[n]

class TestFib(TestCase):
    def test_fib(self):
        n = 5
        expect_result = 12
        self.assertEquals(fib(n), expect_result)
