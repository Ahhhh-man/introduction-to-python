import unittest
# import pytest
from calc import SimpleCalc


class CalcTest(unittest.TestCase):
    calc = SimpleCalc()

    # assertions to write our test cases
    # we will use our basic calc. example to write the test first then the code

    def test_add(self):
        self.assertEqual(self.calc.add(3, 2), 5)  # if True, test would pass, else False

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(3, 2), 1)

    def test_multi(self):
        self.assertEqual(self.calc.multi(2, 2), 4)

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 3), 2)