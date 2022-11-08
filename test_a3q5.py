import unittest
from a3q5_numbers import write_out_number

class TestA3Q4(unittest.TestCase):
    def test_a3q4t1(self):
        self.assertEqual('one hundred twenty three', write_out_number(123))
    def test_a3q4t2(self):
        self.assertEqual('one hundred eleven', write_out_number(111))
    def test_a3q4t3(self):
        self.assertEqual('five hundred seventeen', write_out_number(517))
    def test_a3q4t4(self):
        self.assertEqual('nine hundred ninety nine', write_out_number(999))
    