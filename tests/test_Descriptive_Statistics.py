import unittest
import statistics
import random
from scipy.stats import zscore as scipy_zscore
from src.descriptive_statistics_calculator import DescriptiveStatisticsCalculator


class TestCases(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = DescriptiveStatisticsCalculator()

    def testInstantiateCalculator(self):
        self.assertIsInstance(self.calculator, DescriptiveStatisticsCalculator)

    def testMean(self):
        randomList = []
        for i in range(0, 100000):
            randomNumber = random.randint(0, 1000)
            randomList.append(randomNumber)
        expectedValue = statistics.mean(randomList)
        actualValue = self.calculator.mean(randomList)
        self.assertEqual(expectedValue, actualValue)

    def testMedia(self):
        randomList = []
        for i in range(0, 100000):
            randomNumber = random.randint(0, 1000)
            randomList.append(randomNumber)
        expectedValue = statistics.median(randomList)
        actualValue = self.calculator.median(randomList)
        self.assertEqual(expectedValue, actualValue)

    def testMode(self):
        randomList = []
        for i in range(0, 100000):
            randomNumber = random.randint(0, 1000)
            randomList.append(randomNumber)
        expectedValue = statistics.multimode(randomList)
        actualValue = self.calculator.modes(randomList)
        self.assertEqual(expectedValue, actualValue)

    def testVariance(self):
        randomList = []
        for i in range(0, 100000):
            randomNumber = random.randint(0, 1000)
            randomList.append(randomNumber)
        expectedValue = statistics.pvariance(randomList)
        actualValue = self.calculator.variance(randomList)
        self.assertAlmostEqual(expectedValue, actualValue)

    def testStandardDeviation(self):
        randomList = []
        for i in range(0, 100000):
            randomNumber = random.randint(0, 1000)
            randomList.append(randomNumber)
        expectedValue = statistics.pstdev(randomList)
        actualValue = self.calculator.standardDeviation(randomList)
        self.assertAlmostEqual(expectedValue, actualValue)

    def testZScore(self):
        randomList = []
        for i in range(0, 100000):
            randomNumber = random.randint(0, 1000)
            randomList.append(randomNumber)
        expectedValues = scipy_zscore(randomList)
        actualValues = self.calculator.zScores(randomList)
        self.assertEqual(expectedValues.size, len(actualValues))
        for i in range(0, expectedValues.size):
            self.assertAlmostEqual(expectedValues[i], actualValues[i])

    def testResultProperty(self):
        self.calculator.results.clear()
        self.assertEqual(self.calculator.results, [])


if __name__ == "__main__":
    unittest.main()
