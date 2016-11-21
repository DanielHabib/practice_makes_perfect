"""
Construct all possible subsets
(There are 2^n subsets of a fixed set)

"""



def findSubsets(arr):


    if arr == []: return [[]]

    result = []
    subsets = findSubsets(arr[:-1])
    for value in subsets:
        result.append(value)
        updated = value[:]
        updated.append(arr[-1])
        result.append(updated)
    return result



from unittest import TestCase
from itertools import chain, combinations

def powerset(iterable):
    xs = list(iterable)
    # note we return an iterator rather than a list
    return chain.from_iterable(combinations(xs,n) for n in range(len(xs)+1) )


class TestSubsets(TestCase):
    def test_findSubsets(self):
        args = [1,2,3]
        result = findSubsets(args)
        answer = [list(n) for n in powerset(args)]
        self.assertItemsEqual(result, answer)




