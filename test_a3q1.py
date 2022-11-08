import unittest
from a3q1_anagrams import are_anagrams


class TestA3Q1(unittest.TestCase):
    def test_a3q1t1(self):
        self.assertTrue(are_anagrams('evil', 'live'))
    def test_a3q1t2(self):
        self.assertFalse(are_anagrams('evil', 'livey'))
    def test_a3q1t3(self):
        self.assertTrue(are_anagrams('liSten', 'silenT'))

