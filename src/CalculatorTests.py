import unittest
from Calculator import Calculator
from CsvReader import CsvReader
from pprint import pprint


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        test_data_add = CsvReader('/src/addition.csv').data
        for row in test_data_add:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))

    def test_subtract_method_calculator(self):
        test_data_sub = CsvReader('/src/subtraction.csv').data
        for row in test_data_sub:
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), int(row['Result']))

if __name__ == '__main__':
    unittest.main()
