from STATIC_METHODS.addition import addition
from STATIC_METHODS.subtraction import subtraction
from STATIC_METHODS.multiplication import multiplication
from STATIC_METHODS.division import division
from STATIC_METHODS.squaring import squaring
from STATIC_METHODS.square_rooting import square_rooting
from STATIC_METHODS.inversion import inversion

class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def square(self, a):
        self.result = squaring(a)
        return self.result

    def square_root(self, a):
        self.result = square_rooting(a)
        return self.result

    def inverse(self, a):
        self.result = inversion(a)
        return self.result
