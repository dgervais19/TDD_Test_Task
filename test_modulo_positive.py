# Iteration from test_simp_calc task

# from test_modulo_positive import Simp_Calc
from modulo_positive import Simp_Calc
import unittest
import pytest

# Lets create a class to write our tests

class Calc_test(unittest.TestCase):

# unittest.TestCase works with unittest frame work as a parent class

    calc = Simp_Calc()
# creating an object of our class

# define you test methods
    def test_modulo(self):
        # Checks to see if num1 % num2 == 0
        self.assertEqual(self.calc.modulo(10, 5),  True)
        self.assertEqual(self.calc.modulo(10, 4), False)

        # Checks to see if the inputted numbers are positive
    def test_is_positive(self):
        self.assertEqual(self.calc.is_positive(10, 3), True)
        self.assertEqual(self.calc.is_positive(-10, 6), False)
