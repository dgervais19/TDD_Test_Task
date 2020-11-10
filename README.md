# TDD Test Exercise

### Tasks
1. Create a test to check if the number has remainder 0.
2. Create a class and method to write code to pass the test.
3. Create a test to check if given values are positive.
4. Create a method in the class to pass the test.

### Acceptance Criteria:
* Create a new repo
* Create a new project
* Create a file to write tests
* Create a file to write code
* Implement pseudo coding
* Create a README documenting the steps to successfully achieve the task

### Steps

1. Create a new project in PyCharm and a new repository on GitHub
2. Within the project, create a .gitignore file to ignore irrelevant files.
3. Create a test file and a written code file
4. Install pytest with `pip install pytest`
5. Import all the relevant packages in the test file
```
# Iteration from test_simp_calc task

from modulo_positive import Simp_Calc
import unittest
import pytest
```
6. Create a testing class which is a child of unittest.TestCase
```
class Calc_test(unittest.TestCase):
```
7. Create an object for the class
```
calc = Simp_Calc()
```

8. Define test methods while keeping to the correct naming conventions starting with test_<name>
```
# define you test methods
    def test_modulo(self):
        # Checks to see if num1 % num2 == 0
        self.assertEqual(self.calc.modulo(10, 5),  True)
        self.assertEqual(self.calc.modulo(10, 4), False)

        # Checks to see if the inputted numbers are positive
    def test_is_positive(self):
        self.assertEqual(self.calc.is_positive(10, 3), True)
        self.assertEqual(self.calc.is_positive(-10, 6), False)

```

9. Go to the code file and create a class for the methods.
```
class Simp_Calc:
```

10. Create the functions within a class
    * The modulo function takes the two arguments and returns true if the modulus == 0. If this isn't the case, it returns false
    * the is_positive function checks whether the two arguments are positive numbers or not. If so, return True. If not, return False.
```
    def modulo(self, val_1, val_2):
        if val_1 % val_2 == 0:
            return True
        else:
            return False

    def is_positive(self, val_1, val_2):
        if val_1 > 0 and val_2 > 0:
            return True
        else:
            return False
```

11. Run the test using `python -m pytest` to see if the code works