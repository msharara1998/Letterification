import unittest
from src.main import letterify

class TestLetterify(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(letterify(0), "zero")

    def test_single_digit(self):
        self.assertEqual(letterify(1), "one")
        self.assertEqual(letterify(9), "nine")

    def test_double_digit(self):
        self.assertEqual(letterify(10), "ten")
        self.assertEqual(letterify(15), "fifteen")
        self.assertEqual(letterify(99), "ninety nine")

    def test_triple_digit(self):
        self.assertEqual(letterify(100), "one hundred")
        self.assertEqual(letterify(101), "one hundred one")
        self.assertEqual(letterify(999), "nine hundred ninety nine")

if __name__ == '__main__':
    unittest.main()