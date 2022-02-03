# TDD Task
- create a test to check is the number divisible/remainder 0 if True pass the test if False fail
- create a class and method to write code to pass the test
-  create a test case to calculate % and code to pass the test
- create a test to check if the given values are positive 
- create a method in the class to pass the test

## Tests
- Check 3 is a factor of 9 is True
- Check 3 ≡ 10 mod 7 i.e, 10 % 7 = 3
- Check -7 gives False for non-negative test


## Test code
```python
import unittest
import pytest

from factor import Factor

class CalcTest(unittest.TestCase):
    calc = Factor()

    def test_divisible(self):
        self.assertEqual(self.calc.divisible(9, 3), True)

    def test_modulus(self):
        self.assertEqual(self.calc.modulus(10, 7), 3)

    def test_positive(self):
        self.assertEqual(self.calc.positive(-7), False)
```

## Code to pass test
```python
class Factor:
    def divisible(self, num1, num2):
        return True if num1 % num2 == 0 else False

    def modulus(self, num1, num2):
        return num1 % num2

    def positive(self, num1):
        return True if num1 > 0 else False
```
## Output
```commandline
Testing started at 14:32 ...
Launching unittests with arguments python -m unittest C:/Users/Ahhhh-man/PycharmProjects/python_tdd_task/test.py in C:\Users\Ahhhh-man\PycharmProjects\python_tdd_task



Ran 3 tests in 0.002s

OK

```