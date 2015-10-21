"""A Trie DataStructure"""
from node import TrieNode

from unittest import TestCase


class Trie:
    """Simple Trie Datastructure"""
    def __init__(self, root_val=""):
        self.root = TrieNode(root_val)

    def add_word(self, string):
        current = self.root
        for letter in string:
            if current.children.get(letter, False):
                current = current.children[letter]
            else:
                new_letter = TrieNode(letter)
                current.children[letter] = new_letter
                current = new_letter


class TestTrie(TestCase):

    def test_trie_adds_word(self):
        trie = Trie()
        trie.add_word("mud")
        m_node = trie.root.children["m"]
        u_node = m_node.children["u"]
        d_node = u_node.children["d"]

        self.assertEquals(m_node.data, "m")
        self.assertEquals(u_node.data, "u")
        self.assertEquals(d_node.data, "d")
        self.assertEquals(d_node.children, {})

    def test_trie_adds_words_with_letter_repeat(self):
        trie = Trie()
        trie.add_word("mum")
        m_node = trie.root.children["m"]
        u_node = m_node.children["u"]
        m2node = u_node.children["m"]
        self.assertEquals(m_node.data, "m")
        self.assertEquals(u_node.data, "u")
        self.assertEquals(m2node.data, "m")
        self.assertEquals(m2node.children, {})
