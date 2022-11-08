import unittest
from a3q3_texting import message_to_keys


class TestA3Q3(unittest.TestCase):
    def test_a3q3t1(self):
        self.assertEqual('4433555555666110966677755531111', message_to_keys("Hello, World!"))
    def test_a3q3t2(self):
        self.assertEqual('83377778444664022222202222221111', message_to_keys("Testing abc abc!"))
    def test_a3q3t3(self):
        self.assertEqual('8443307788444222550227776669660333666990588677777066688833777084433055529999999036664', message_to_keys('The quick brown fox jumps over the lazy dog'))
    def test_a3q3t4(self):
        self.assertEqual('212211222111311113311111333', message_to_keys("A.B,C?D!E:F"))