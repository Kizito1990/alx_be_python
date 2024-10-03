#!/bin/bash
import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):


    def test_addition(self):
        self.calc = SimpleCalculator()
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)

    def test_subtraction(self):
        self.calc = SimpleCalculator()
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(-1, -1), 0)

    def test_multiplication(self):
        self.calc = SimpleCalculator()
        self.assertEqual(self.calc.multiply(10, 5), 50)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(-1, -1), 1)

    def test_division(self):
        self.calc = SimpleCalculator()
        self.assertEqual(self.calc.divide(10, 5), 2)
        self.assertEqual(self.calc.divide(-1, 1), -1)
        self.assertEqual(self.calc.divide(-1, -1), 1)

        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10, 0)


if __name__ == '__main__':
    unittest.main()
