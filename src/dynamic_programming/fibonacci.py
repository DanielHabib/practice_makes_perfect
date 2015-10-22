from unittest import TestCase
#Recursive Without Memoiztion
def fib_no_memo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n -  1) + fib(n - 2)

# Recursion with Memoization
memo = {}
def fib(n, memo):
    if n in memo:
        return memo[n]
    if n == 1 or n == 2:
        return 1

    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

# Using a wrapper
class Memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, arg):
        if arg not in self.memo:
            self.memo[arg] = self.fn(arg)
            return self.memo[arg]

@Memoize
def fib_wrapper(n):
    a,b = 1,1
    for i in range(n-1):
        a, b = b, a+b
    return a

class TestFib(TestCase):

    def test_simple_fib_works(self):
        answer = fib(3, {})
        self.assertEquals(answer, 2)

    def test_large_fib_works(self):
        answer = fib(8, {})

        self.assertEquals(answer, 21)
