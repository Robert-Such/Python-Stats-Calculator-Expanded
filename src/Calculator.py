from CsvReader import CsvReader


def addition(a, b):
    a = int(a)
    b = int(b)
    return a + b


def subtraction(c, d):
    c = int(c)
    d = int(d)
    return d - c


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