import unittest
from SOURCE.Statistics import Statistics
from SOURCE.CsvReaderForStats import CsvReaderForStats


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.StatCal = Statistics()
        self.StatData = CsvReaderForStats('DATA/statsdata.csv')
        self.TestValues = self.StatData.column['TestValues']

    def test_instantiate_statistics(self):
        self.assertIsInstance(self.StatCal, Statistics)

    def test_method_mean(self):
        ExpectedMean = float(self.StatData.column['ExpectedMean'][0])
        self.assertEqual(self.StatCal.mean(self.TestValues), ExpectedMean)

    def test_method_median(self):
        ExpectedMedian = float(self.StatData.column['ExpectedMedian'][0])
        self.assertEqual(self.StatCal.median(self.TestValues), ExpectedMedian)

    def test_method_mode(self):
        ExpectedMode = float(self.StatData.column['ExpectedMode'][0])
        self.assertEqual(self.StatCal.mode(self.TestValues), ExpectedMode)

    def test_method_standard_deviation(self):
        ExpectedStandardDeviation = float(self.StatData.column['ExpectedStandardDeviation'][0])
        self.assertEqual(self.StatCal.standard_deviation(self.TestValues), ExpectedStandardDeviation)

    def test_method_variance(self):
        ExpectedVariance = float(self.StatData.column['ExpectedVariance'][0])
        self.assertEqual(self.StatCal.variance(self.TestValues), ExpectedVariance)




