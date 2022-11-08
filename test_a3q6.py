import unittest
from a3q6_bingo import generate_bingo_card

class TestA3Q6(unittest.TestCase):
    def test_a3q6t1(self):
        self.assertIn('B', generate_bingo_card())
        self.assertEqual(5, len(generate_bingo_card()['B']))
        for n in generate_bingo_card()['B']:
            self.assertGreaterEqual(n,1)
            self.assertLessEqual(n,15)
    def test_a3q6t2(self):
        self.assertIn('I', generate_bingo_card())
        self.assertEqual(5, len(generate_bingo_card()['I']))
        for n in generate_bingo_card()['I']:
            self.assertGreaterEqual(n,16)
            self.assertLessEqual(n,30)
    def test_a3q6t3(self):
        self.assertIn('N', generate_bingo_card())
        self.assertEqual(5, len(generate_bingo_card()['N']))
        for n in generate_bingo_card()['N']:
            self.assertGreaterEqual(n,31)
            self.assertLessEqual(n,45)
    def test_a3q6t4(self):
        self.assertIn('G', generate_bingo_card())
        self.assertEqual(5, len(generate_bingo_card()['G']))
        for n in generate_bingo_card()['G']:
            self.assertGreaterEqual(n,46)
            self.assertLessEqual(n,60)
    def test_a3q6t5(self):
        self.assertIn('O', generate_bingo_card())
        self.assertEqual(5, len(generate_bingo_card()['O']))
        for n in generate_bingo_card()['O']:
            self.assertGreaterEqual(n,61)
            self.assertLessEqual(n,75)
    def test_a3q6t6(self):
        self.assertEqual(5, len(generate_bingo_card()))