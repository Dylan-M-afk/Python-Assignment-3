import unittest
from a3q2_scrabble import get_scrabble_score_for_word


class TestA3Q2(unittest.TestCase):
    def test_a3q2t1(self):
        self.assertEqual(22, get_scrabble_score_for_word('quiz'))
    def test_a3q2t2(self):
        self.assertEqual(33, get_scrabble_score_for_word('jazzy'))
    def test_a3q2t3(self):
        self.assertEqual(10, get_scrabble_score_for_word('monty'))
    def test_a3q2t4(self):
        self.assertEqual(14, get_scrabble_score_for_word('python'))

    