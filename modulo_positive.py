# This file will be used to see if a number is divisible/remainder 0

class Simp_Calc:

    def add(self, val_1, val_2):
        return val_1 + val_2

    def subtract(self, val_1, val_2):
        return val_1 - val_2

    def multiply(self, val_1, val_2):
        return val_1 * val_2

    def divide(self, val_1, val_2):
        return val_1 / val_2

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


if __name__ == '__main__':

    calc = Simp_Calc()

    print(calc.is_positive(10,10))
    print(calc.modulo(12, 5))

