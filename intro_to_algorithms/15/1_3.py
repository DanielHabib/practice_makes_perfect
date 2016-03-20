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

    def cut_pipe(self, n):

        # base case
        if n <= 0:
            return 0

        q = -10000

        # check for sub problem
        if self.memo.get(n, False):
            return self.memo[n]
        for i in range(n):
            i += 1
            # Be sure to account for not cutting. if i == n
            cost = self.cost
            if i == n:
                cost = 0
            q = max(q, self.cut_pipe(n - i) + self.price_dict[i] - cost)

        # store sub problem
        self.memo[n] = q
        return q


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
        self.assertEquals(val, self.price_dict[8])






