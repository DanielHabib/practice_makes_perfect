"""
Generate all Permuataions
(There are N! permutations)
"""


def allPermutations(string):
     if string == "":
         return [[]]
     totalPermutations = []
     for index, char in enumerate(string):
         permutations = allPermutations(string[:index]+ string[index+1:])
         [permutation.append(char) for permutation in permutations]
         [totalPermutations.append(permutation) for permutation in permutations]
     return totalPermutations



from unittest import TestCase
import itertools

class TestAllPermutations(TestCase):
    def test_allPermutations(self):
        args = "abc"
        answer = [list(x) for x in itertools.permutations(args)]
        result = allPermutations(args)
        self.assertItemsEqual(answer, result)
