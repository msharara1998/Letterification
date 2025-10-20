import unittest
from src.main import letterify, letterify_ar

class TestLetterify(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(letterify(0), "zero")

    def test_single_digit(self):
        self.assertEqual(letterify(1), "One")
        self.assertEqual(letterify(9), "Nine")

    def test_double_digit(self):
        self.assertEqual(letterify(10), "Ten")
        self.assertEqual(letterify(15), "Fifteen")
        self.assertEqual(letterify(99), "Ninety nine")

    def test_triple_digit(self):
        self.assertEqual(letterify(100), "One hundred")
        self.assertEqual(letterify(101), "One hundred one")
        self.assertEqual(letterify(999), "Nine hundred ninety nine")


class TestLetterifyArabic(unittest.TestCase):
    def test_zero_ar(self):
        self.assertEqual(letterify_ar(0), "صفر")

    def test_single_digit_ar(self):
        self.assertEqual(letterify_ar(1), "واحد")
        self.assertEqual(letterify_ar(9), "تسعة")

    def test_double_digit_ar(self):
        self.assertEqual(letterify_ar(10), "عشرة")
        self.assertEqual(letterify_ar(15), "خمسة عشر")
        self.assertEqual(letterify_ar(99), "تسعون و تسعة")

    def test_triple_digit_ar(self):
        self.assertEqual(letterify_ar(100), "مئة")
        self.assertEqual(letterify_ar(200), "مئتان")
        self.assertEqual(letterify_ar(356), "ثلاثمئة و خمسون و ستة")

    def test_thousands_ar(self):
        self.assertEqual(letterify_ar(1000), "واحد و ألف")
        self.assertEqual(letterify_ar(100001), "مئة و ألف و واحد")

    def test_large_numbers_ar(self):
        # Testing a large number
        result = letterify_ar(13_356_100_001)
        self.assertIn("مليار", result)
        self.assertIn("مليون", result)
        self.assertIn("ألف", result)

if __name__ == '__main__':
    unittest.main()