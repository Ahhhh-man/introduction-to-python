import unittest
#import pytest

from factor import Factor


class CalcTest(unittest.TestCase):
    calc = Factor()

    def test_divisible(self):
        self.assertEqual(self.calc.divisible(9, 3), True)

    def test_modulus(self):
        self.assertEqual(self.calc.modulus(10, 7), 3)

    def test_positive(self):
        self.assertEqual(self.calc.positive(-7), False)