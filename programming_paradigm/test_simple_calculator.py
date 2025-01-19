import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(9, 0), 9)
        self.assertEqual(self.calc.add(3, -3), 0)

    def test_subtraction(self):
        """Test the subtraction method"""
        self.assertEqual(self.calc.subtract(0, -2), 2)
        self.assertEqual(self.calc.subtract(-20, -50), 30)
        self.assertEqual(self.calc.subtract(5, 2), 3)
        self.assertEqual(self.calc.subtract(-2, 4), -6)

    def test_multiplication(self):
        """Test the multiplication method"""
        self.assertEqual(self.calc.multiply(2, 0), 0)
        self.assertEqual(self.calc.multiply(4, 2), 8)
        self.assertEqual(self.calc.multiply(-2, 2), -4)
        self.assertEqual(self.calc.multiply(-5, -5), 25)

    def test_division(self):
        """Test the division method"""
        self.assertEqual(self.calc.divide(2, 0), None)
        self.assertEqual(self.calc.divide(0, 2), 0)
        self.assertEqual(self.calc.divide(2, 2), 1)
        self.assertEqual(self.calc.divide(-2, 2), -1)
        self.assertEqual(self.calc.divide(-2, -2), 1)


        
