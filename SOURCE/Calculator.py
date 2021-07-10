from addition import addition
from subtraction import subtraction
from multiplication import multiplication
from division import division
from squaring import squaring
from square_rooting import square_rooting
from inversion import inversion

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
