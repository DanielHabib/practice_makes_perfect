"""Build Order Problem"""
from unittest import TestCase
"""

"""
def get_build_order(vals, dependencies):
    """
        NOTES: loop through the vals, picking dependencies apart.
        BF:
    """

class TestDependencyProblem(TestCase):

    def test_simple_dependency(self):
        vals = ['a', 'b', 'c', 'd', 'e']

        dependencies = {'a': ['b'],
                        'c': ['b', 'a'],
                        'd': ['c', 'a'],
                        'e': ['c', 'd']}

        build_order = get_build_order(vals, dependencies)

        self.assertEqual(build_order, ['b', 'a', 'c', 'd', 'e'])
