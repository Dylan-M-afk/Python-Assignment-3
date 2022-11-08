import unittest
from a3q4_postal_codes import get_details_from_postal_code

class TestA3Q4(unittest.TestCase):
    def test_a3q4t1(self):
        self.assertEqual(['Newfoundland', 'urban'], get_details_from_postal_code('A1A 2B3'))
    def test_a3q4t2(self):
        self.assertEqual(['Nunavut or Northwest Territories', 'rural'], get_details_from_postal_code('X0A 5B3'))
    def test_a3q4t3(self):
        self.assertEqual(["Alberta", 'urban'], get_details_from_postal_code('T2A 1Q2'))
    def test_a3q4t4(self):
        self.assertEqual(["Ontario", 'urban'], get_details_from_postal_code('M3A 1Q2'))
    def test_a3q4t5(self):
        self.assertEqual(["Quebec", 'urban'], get_details_from_postal_code('H4A 1Q2'))