""" Unit & Integration Tests for Test Unique string characters"""

import unittest
import mock

import strings.unique_string_characters as task



class TestUniqueCharacters(unittest.TestCase):
    """ Testing Unique Characters class with both Unit and Integration """
    def setUp(self):
        """ Initialize """
        self._class = task.UniqueCharacters()

    def tearDown(self):
        """ Tear it down """

    def test_initial_attempt_unique_string(self):
        """ Test the initial attempt with a unique string """
        input_string = 'DerEcK Zo0l&nd'
        rez = self._class.initial_attempt(input_string)
        assert rez

    def test_initial_attempt_non_unique_string(self):
        """ Test the initial attempt with different non-unique string """
        input_string = 'DerEcK Zo0l&ndEr '
        rez = self._class.initial_attempt(input_string)
        assert not rez

        input_string = 'ddddddddd '
        rez = self._class.initial_attempt(input_string)
        assert not rez

        input_string = '    '
        rez = self._class.initial_attempt(input_string)
        assert not rez

        input_string = ''
        rez = self._class.initial_attempt(input_string)
        assert not rez

    def test_with_try_catch_with_unique_string(self):
        """ Test Unique String without a try catch"""
        input_string = 'DerEcK Zo0l&nd'
        rez = self._class.without_the_try_catch(input_string)
        assert rez

    def test_without_try_catch_with_unique_string(self):
        """ Test the initial attempt with different non-unique string """
        input_string = 'DerEcK Zo0l&ndEr '
        rez = self._class.without_the_try_catch(input_string)
        assert not rez

        input_string = 'ddddddddd '
        rez = self._class.without_the_try_catch(input_string)
        assert not rez

        input_string = '    '
        rez = self._class.without_the_try_catch(input_string)
        assert not rez

        input_string = ''
        rez = self._class.without_the_try_catch(input_string)
        assert not rez

    def test_merge_sort(self):
        """ Test Merge Sort """
        unsorted = [3, 2, 4, 1]
        sorted_list = [1, 2, 3, 4]
        self._class.merge_sort_first_attempt(unsorted)
        self.assertEquals(sorted_list, unsorted)

