from SOURCE.Calculator import Calculator
from STATIC_METHODS.mean import mean
from STATIC_METHODS.median import median


class Statistics(Calculator):
    data = []

    def __init__(self):
        super().__init__()

    def mean(self, data):
        self.result = mean(data)
        return self.result

    def median(self, data):
        self.result = median(data)
        return self.result

    def mode(self, data):
        self.result = mode(data)
        return self.result

    def variance(self, data):
        self.result = variance(data)
        return self.result

    def standard_deviation(self, data):
        self.result = standard_deviation(data)
        return self.result
