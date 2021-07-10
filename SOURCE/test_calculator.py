import unittest
from Calculator import Calculator
from CsvReader import CsvReader


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        test_data = CsvReader('DATA/addition.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), float(row['Result']))

    def test_subtract_method_calculator(self):
        test_data = CsvReader('DATA/subtraction.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), float(row['Result']))

    def test_multiply_method_calculator(self):
        test_data = CsvReader('DATA/multiplication.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), float(row['Result']))

    def test_divide_method_calculator(self):
        test_data = CsvReader('DATA/division.csv').data
        for row in test_data:
            self.assertAlmostEqual(self.calculator.divide(row['Value 1'], row['Value 2']), float(row['Result']))

    def test_square_method_calculator(self):
        test_data = CsvReader('DATA/square.csv').data
        for row in test_data:
            self.assertAlmostEqual(self.calculator.square(row['Value 1']), float(row['Result']))

    def test_square_root_method_calculator(self):
        test_data = CsvReader('DATA/square_root.csv').data
        for row in test_data:
            self.assertAlmostEqual(self.calculator.square_root(row['Value 1']), float(row['Result']))

    def test_inverse_method_calculator(self):
        test_data = CsvReader('DATA/inverse.csv').data
        for row in test_data:
            self.assertAlmostEqual(self.calculator.inverse(row['Value 1']), float(row['Result']))


if __name__ == '__main__':
    unittest.main()
