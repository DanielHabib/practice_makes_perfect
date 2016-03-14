"""This Problem was found in the `Intro To Algo` textbook"""
from unittest import TestCase

class PipeOptimization:

    def __init__(self, p_index):
        """

        Args:
            p_index (dict): Maintains the table that contains correlating length to value of that piece

        """
        self.p_index = p_index
        self.store = {}

    def max_profit(self, n):
        """

        Args:
            n (int): Represents the length of the pipe


        Returns: int, the maximum possible value that can be attained from any given piece of pipe
            and associated price table


        Notes:
            One thing is we have an unlimited number of each type of cut which makes it easier.
            We dont have to worry about how many coins we have left or whatever.

            The method of cutting up the input. Here we need to try all possible cuts within the
            length of the pipe each time if we want a shot.

        """
        # Base Case
        if n <= 0:
            return 0

        # Memoize
        if n in self.store.keys():
            return self.store[n]
        q = 0
        for i in range(1, n + 1):
            current_cut_value = 0
            if i in self.p_index.keys():
                current_cut_value = self.p_index[i]

            q = max(q, current_cut_value + self.max_profit(n - i))
        self.store[n] = q
        return q


class PipeOptimizationTest(TestCase):

    def setUp(self):
        self.p_dict = {1: 1,
                       2: 3,
                       3: 4,
                       4: 4}

    def test_max_profit(self):

        pipe = PipeOptimization(self.p_dict)
        result = pipe.max_profit(4)
        print(pipe.store)
        self.assertEquals(result, 6)

    def test_max_profit_base_case(self):

        pipe = PipeOptimization(self.p_dict)
        result = pipe.max_profit(1)

        self.assertEquals(result, 1)

    def test_store_is_fully_constructed(self):

        pipe = PipeOptimization(self.p_dict)
        n = 4
        pipe.max_profit(n)
        for i in range(1, n + 1):
            self.assertTrue(i in pipe.store.keys())



