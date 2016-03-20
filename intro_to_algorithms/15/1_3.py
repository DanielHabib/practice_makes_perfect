# -*- coding: utf-8 -*-
from unittest import TestCase
"""
Consider a modification of the rod-cutting problem in which, in addition to a
price pi for each rod, each cut incurs a fixed cost of c. The revenue associated with
a solution is now the sum of the prices of the pieces minus the costs of making the
cuts. Give a dynamic-programming algorithm to solve this modified problem.

Notes:
      In addition to the normal problem we now also have to worry about the cost of cutting a piece.
      The good news is we can still maintain the same structure of referencing sub problems solutions.
      because once an optimal solution has been solved for, we can reuse it. This includes the cost
      of the cut.

      So the real trick, is to also consider the cut cost into the solution. c is a
      constant just think about it when the cut occurs

"""


class CutPipe:
    def __init__(self, price_dict, cost):
        self.price_dict = price_dict
        self.cost = cost
        self.memo = {}
        self.cuts = []

    def cut_pipe(self, n):
        val, cuts = self.cut_pipe_help(n)
        self.cuts = cuts
        return val

    def cut_pipe_help(self, n):
        # base case

        if n <= 0:
            return 0, []

        # intialize variables
        q = -10000
        big_i = 0
        big_cuts = []

        # check for sub problem
        if self.memo.get(n, False):

            return self.memo[n]

        # Create Logic for Calling Sub problem
        for i in range(n):
            i += 1
            # Be sure to account for not cutting. if i == n
            cost = self.cost
            if i == n:
                cost = 0
            # Call Sub problem

            val, cuts = self.cut_pipe_help(n - i)

            val += self.price_dict[i] - cost
            if val > q:
                q = val
                big_i = i
                big_cuts = cuts
        # Store The Current Cut

        # self.cuts.append(big_i)
        big_cuts.append(big_i)
        # store sub problem
        self.memo[n] = (q, big_cuts)

        # Return Solution
        return q, big_cuts


class TestCutPipe(TestCase):
    def setUp(self):
        self.price_dict = {
            1: 1,
            2: 1.8,
            3: 2.1,
            4: 7.6,
            5: 10,
            6: 11,
            7: 11.5,
            8: 12,
        }

    def test_cut_pipe(self):
        cost = 2
        cutter = CutPipe(self.price_dict, cost)
        val = cutter.cut_pipe(8)
        # There is only 1 cut so we can subtract cost
        self.assertEquals(val, 15.2 - cost)

    def test_cut_with_no_cuts(self):
        cost = 2
        cutter = CutPipe(self.price_dict, cost)
        val = cutter.cut_pipe(5)
        # There aren't any cuts
        self.assertEquals(val, 10)

    def test_memo_solves_sub_problems(self):
        cost = 2
        n = 5
        cutter = CutPipe(self.price_dict, cost)
        cutter.cut_pipe(n)

        self.assertEquals(len([x for x in cutter.memo.keys()]), n)

    def test_cutting_with_high_cost_reduces_cuts(self):
        cost = 8
        cutter = CutPipe(self.price_dict, cost)
        val = cutter.cut_pipe(8)
        sum_value = 0
        for cut in cutter.cuts:
            sum_value += self.price_dict[cut]
        self.assertEquals(val, self.price_dict[8])
        self.assertEquals([8], cutter.cuts)
        self.assertEquals(val, sum_value - (len(cutter.cuts) - 1) * cost)


    def test_cuts_are_stored_correctly(self):
        cost = 1
        cutter = CutPipe(self.price_dict, cost)
        val = cutter.cut_pipe(8)
        sum_value = 0
        for cut in cutter.cuts:
            sum_value += self.price_dict[cut]
        self.assertEquals([4, 4], cutter.cuts)
        self.assertEquals(val, sum_value - (len(cutter.cuts) - 1) * cost)
