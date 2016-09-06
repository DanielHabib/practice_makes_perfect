import unittest
from unittest_data_provider import data_provider

def find_median(n, m):

    n_floor = 0
    n_ceil = len(n) - 1
    m_floor = 0
    m_ceil = len(m) - 1


    while True:
        current_n = (n_ceil + n_floor) // 2
        current_m = (m_ceil + m_floor) // 2
        n_length = n_ceil - n_floor
        m_length = m_ceil - m_floor
        if n_length == 1 and m_length == 1:
            a = max(n[n_floor], m[m_floor])
            b = min(n[n_ceil], m[m_ceil])
            return (a + b) / 2
        if n_length == 0 and m_length == 0:
            return (n[n_ceil] + m[m_floor])/2

        if n[current_n] == m[current_m]:
            return n[current_n]

        if n[current_n] > m[current_m]:
            print 'n current is greater than m current\n_______________'
            m_floor = current_m
            n_ceil = current_n
        else: # n[current+n] < m[current_m]
            print 'n current is less than m current\n_______________'
            m_ceil = current_m
            n_floor = current_n


class TestFindMedian(unittest.TestCase):

    tests = (
        ([1,2,3,4,5], [1,2,3,4,5] , 3), # Test initial base case
        ([1,1,1,4,5], [1,2,6,8,9] , 3), # Test the base case of both len(arrays) == 2
        ([1,1,1,2,4,5], [1,2,16,18,19,20] , 2), # Test Same Even length of values
        # What if one list is really really long

    )

    def test_find_median(self):
        for a, b ,expectedResult in self.tests:
            result = find_median(a, b)
            self.assertEquals(result, expectedResult)
