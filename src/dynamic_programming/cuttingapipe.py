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

    def max_profit(self, n, price_so_far):
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
        # Base Cases
        if n <= 0:
            return price_so_far

        max_value = 0
        if n in self.p_index.keys():
            max_value = self.p_index[n]

        # if self.store.get(n, False):
        #     return self.store[n]

        for length in range(n):
            length += 1

            updated_price = price_so_far + self.p_index.get(length, 0)

            max_value = max(
                    self.max_profit(n - length, updated_price),
                    max_value)
        # Recall loop

        print(max_value)

        self.store[n] = max_value

        return max_value


class PipeOptimizationTest(TestCase):

    def setUp(self):
        self.p_dict = {1: 1,
                       2: 3,
                       3: 4,
                       4: 4}

    def test_max_profit(self):

        pipe = PipeOptimization(self.p_dict)
        result = pipe.max_profit(4, 0)
        print(pipe.store)
        self.assertEquals(result, 6)

    def test_max_profit_base_case(self):

        pipe = PipeOptimization(self.p_dict)
        result = pipe.max_profit(1, 0)

        self.assertEquals(result, 1)
