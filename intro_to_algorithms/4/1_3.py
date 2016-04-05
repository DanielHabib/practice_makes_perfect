"""Implement both Brute force and recursive algorithms for max-subarray
"""
from unittest import TestCase

def brute_force(arr):

    max_sub = [-1, -1, 0]
    max_sum = float('-inf')

    for i in range(len(arr)):
        c_sum = 0
        for j in range(i, len(arr)):
            c_sum += arr[j]
            if c_sum > max_sum:
                max_sum = c_sum
                max_sub = [i, j, max_sum]
    return tuple(max_sub)


def recursive(arr):
    return recursive_helper(arr, 0, len(arr) - 1)

def recursive_helper(arr, i, j):
    # Recursion => Base Case
    if i == j:
        return i, j, arr[i]

    mid = (i + j) // 2

    left_subarray = recursive_helper(arr, i, mid)
    right_subarray = recursive_helper(arr, mid + 1, j)
    crossover = crossover_helper(arr, i, mid, j)

    if left_subarray[2] > right_subarray[2] and left_subarray[2] > crossover[2]:
        return left_subarray

    if right_subarray[2] > crossover[2]:
        return right_subarray

    return crossover

def crossover_helper(arr, i, mid, j):

    # Calculate from the middle

    ii = mid

    # left first
    c_sum = 0
    max_left = 0
    left_index = mid

    while ii >= 0:
        el = arr[ii]
        c_sum += el
        if c_sum > max_left:
            max_left = c_sum
            left_index = ii
        ii -= 1

    # right next
    jj = mid + 1
    c_sum = 0
    max_right = 0
    right_index = mid

    while jj < len(arr):
        el = arr[jj]
        c_sum += el
        if c_sum > max_right:
            max_right = c_sum
            right_index = jj
        jj += 1

    # return correct
    return left_index, right_index, (max_left + max_right)







class MaxSubArrayTest(TestCase):
    def test_brute_force_works(self):
        arr = [1, -20, 3, 4, 5]
        expected_result = (2, 4, 12)
        result = brute_force(arr)
        self.assertEquals(result, expected_result)


    def test_brute_force_works_with_whole_array(self):
        arr = [1, 20, 3, 4, 5]
        expected_result = (0, 4, 33)

        result = brute_force(arr)

        self.assertEquals(result, expected_result)


    def test_brute_force_works_with_empty_array(self):
        arr = []
        expected_result = (-1, -1, 0)

        result = brute_force(arr)

        self.assertEquals(result, expected_result)


    def test_recursive_works(self):
        arr = [1, -20, 3, 4, 5]
        expected_result = (2, 4, 12)
        result = recursive(arr)
        self.assertEquals(result, expected_result)

    def test_crossover_helper(self):
        arr = [1, -20, 3, 4, 5]

        result = crossover_helper(arr, 0, 2, len(arr) - 1)

        self.assertEquals(result[0], 2)
        self.assertEquals(result[1], 4)
        self.assertEquals(result[2], 12)


