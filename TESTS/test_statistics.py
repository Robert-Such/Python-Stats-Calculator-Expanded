import unittest
import statistics  # python library to compute mean and compare against independently derived value
from SOURCE.Statistics import Statistics
from SOURCE.CsvReaderForStats import CsvReaderForStats
from STATIC_METHODS.randomdata import randomdata


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.StatCal = Statistics()
        # Setup data source from CSV file
        self.StatData = CsvReaderForStats('DATA/statsdata.csv')
        self.TestValues = self.StatData.column['TestValues']
        # Setup for random data
        SeedRangeStart = 5  # Start of seed range
        SeedRangeEnd = 12   # End of seed range
        Array_Length = 50   # Total number of random values to be produced
        MinValue = 108      # Min possible value to be produced
        MaxValue = 1000     # Max possible value to be produced
        self.RandomData = randomdata(SeedRangeStart, SeedRangeEnd, Array_Length, MinValue, MaxValue)

    def test_instantiate_statistics(self):
        self.assertIsInstance(self.StatCal, Statistics)

    def test_method_mean(self):
        # Pull expected mean from stats data spreadsheet
        ExpectedMean = float(self.StatData.column['ExpectedMean'][0])
        # Calculate mean using home grown method against test values in stats data CSV file
        # Then determine if the calculated value is same as the expected value in the CSV file
        self.assertEqual(self.StatCal.mean(self.TestValues), ExpectedMean)
        # Calculate mean using home grown method and python library method against randomly generated values
        # Then determine if the result from both methods match
        self.assertEqual(self.StatCal.mean(self.RandomData), round(statistics.mean(self.RandomData), 4))

    def test_method_median(self):
        # Pull expected median from stats data spreadsheet
        ExpectedMedian = float(self.StatData.column['ExpectedMedian'][0])
        # Calculate median using home grown method against test values in stats data CSV file
        # Then determine if the calculated value is same as the expected value in the CSV file
        self.assertEqual(self.StatCal.median(self.TestValues), ExpectedMedian)
        # Calculate median using home grown method and python library method against randomly generated values
        # Then determine if the result from both methods match
        self.assertEqual(self.StatCal.median(self.RandomData), statistics.median(self.RandomData))

    def test_method_mode(self):
        # Pull expected mode from stats data spreadsheet
        ExpectedMode = float(self.StatData.column['ExpectedMode'][0])
        # Calculate mode using home grown method against test values in stats data CSV file
        # Then determine if the calculated value is same as the expected value in the CSV file
        self.assertEqual(self.StatCal.mode(self.TestValues), ExpectedMode)
        # Calculate mode using home grown method and python library method against randomly generated values
        # Then determine if the result from both methods match
        self.assertEqual(self.StatCal.mode(self.RandomData), statistics.mode(self.RandomData))

    def test_method_standard_deviation(self):
        ExpectedStandardDeviation = float(self.StatData.column['ExpectedStandardDeviation'][0])
        self.assertEqual(self.StatCal.standard_deviation(self.TestValues), ExpectedStandardDeviation)

    def test_method_variance(self):
        ExpectedVariance = float(self.StatData.column['ExpectedVariance'][0])
        self.assertEqual(self.StatCal.variance(self.TestValues), ExpectedVariance)




