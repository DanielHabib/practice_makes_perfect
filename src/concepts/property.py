"""Build confidence with @property"""
from unittest import TestCase


class Foo:
    __slots__ = ["_children"]
    def __init__(self, children=None):

        self._children = children

    @property
    def children(self):
        return self._children

    @children.setter
    def children(self, children):
        self._children = children

    def add_child(self, child):
        self.children.append(child)

    def add_child_private(self, child):
        self._children.append(child)


class FooTest(TestCase):
    def test_adding_children_to_exisiting_array(self):
        """
        Learnings:
            Python allows some fleibility here.
            We are able to append to the 'property' and we are able to append
            to the private variable associated with it.

            I wonder how this works if __slots__ is invoked.

            Just tested it out, __slots__ must point to the private _children
            which makes sense, would have freaked me out a little if it didnt

            Can an array given a certain allocation of memory from __slots__
            grow infiinitely? I believe so because I think it just prevents
            the creation of other properties, not limit the amount allocated
            to this specific property
         """
        foo = Foo()
        arr = [1, 2, 3, 4]
        foo.children = arr[:]
        self.assertEqual(arr, foo.children)
        foo.children.append(5)
        arr.append(5)
        self.assertEqual(arr, foo.children)
        foo.add_child(6)
        arr.append(6)
        self.assertEqual(arr, foo.children)
        foo.add_child_private(7)
        arr.append(7)
        self.assertEqual(arr, foo.children)
