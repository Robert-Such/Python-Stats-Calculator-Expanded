import math

def addition(a, b):
    return float(a) + float(b)

def subtraction(a, b):
    return float(b) - float(a)

def multiplication(a , b):
    return float(a) * float(b)

def division(a , b):
    return float(b) / float(a)

def squaring(a):
    return float(a) * float(a)

def square_rooting(a):
    return math.sqrt(float(a))

def inversion(a):
    return 1 / float(a)


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
