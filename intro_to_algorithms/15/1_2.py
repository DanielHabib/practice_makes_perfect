from unittest import TestCase
"""
Show, by means of a counterexample, that the following “greedy” strategy does
not always determine an optimal way to cut rods.
Define the density of a rod of
length i to be pi=i, that is, its value per inch. The greedy strategy for a rod of
length n cuts off a first piece of length i, where 1  i  n, having maximum
density. It then continues by applying the greedy strategy to the remaining piece of
length n  i .

Notes:
      Greedy Strategy maximizes the price-per-inch(ppi) every time it cuts . Then this method continues
      by applying the same idea to whatever remains on the pipe.

      Prove this doesn't work via counter example.

      Example: if you a have a rod of length 8 and the ppi of a rod of length 5 is 2 and a rod of
        length 3 is 1, you will have a total value of 13. BUT if a cut of length 4 has a value of
        1.9, then you can achieve a value of 15.2
"""


class GreedyPipeCutting:
    def __init__(self, price_dict):
        for key, val in price_dict.items():
            price_dict[key] = val / key
        self.price_dict = price_dict

    def cut_pipe(self, n):
        """Greedy Algo

        1. Recreate dict off if price per inch
        2. Apply Greedy Algo.

        Code:
            Write, then memoize where possible
        """

        # Find the Greediest cut
        best_cut = 0
        for i in range(n):
            i += 1
            best_cut = max(best_cut, self.price_dict.get(i, 0))

        # apply cut
        return self.price_dict[best_cut] + self.cut_pipe(n - best_cut)


class TestGreedyPipeCutting(TestCase):

    def test_cute_pipe(self):
        price_dict = {
            1: 1,
            2: 2,
            3: 3,
            4: 7.6,
            5: 10,
            6: 11,
            7: 11.5,
            8: 12,
        }
        cutter = GreedyPipeCutting(price_dict)

        val = cutter.cut_pipe(8)
        # proves the right value cannot be attained always through greedy in this situation
        self.assertNotEquals(val, 15.2)
