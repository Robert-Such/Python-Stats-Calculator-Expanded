from CsvReader import CsvReader


def addition(a, b):
    return int(a) + int(b)


def subtraction(a, b):
    return int(b) - int(a)

def multiplication(a , b):
    return int(a) * int(b)


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
