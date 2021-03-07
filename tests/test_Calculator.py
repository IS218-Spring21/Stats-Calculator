# Move Imports to fileReader.py ^^
import unittest

# the .py file name is Calculator and the class name is also Calculator

# Move Section to fileReader.py
from src.calculator import Calculator

from tests.src.CSVReader import readCSV

'''
This is the TestCase class that test Calculator class functions.
'''


class TestCalculator(unittest.TestCase):
    # this is the Calculator class instance.
    calculator = None

    # class level setup function, execute once only before any test function.
    @classmethod
    def setUpClass(cls):
        print('')
        print('setUpClass')

    # class level setup function, execute once only after all test function's execution.
    @classmethod
    def tearDownClass(cls):
        print('')
        print('tearDownClass')

    # execute before every test case function run.
    def setUp(self):
        self.calculator = Calculator()
        print('')
        print('setUp')

    # execute after every test case function run.
    def tearDown(self):
        # release the Calculator object.
        if self.calculator is not None:
            self.calculator = None
        print('')
        print('tearDown')

    # below are function that test Calculator class's plus, minus, multiple and divide functions.
    def testInstantiateCalculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def testAddition(self):
        rows = readCSV("tests/testCases/Addition.csv")
        for row in rows:
            expectedResult = float(row["Result"])
            x = float(row["Value 1"])
            y = float(row["Value 2"])
            self.assertEqual(self.calculator.add(x, y), expectedResult)

    def testSubtraction(self):
        rows = readCSV("tests/testCases/Subtraction.csv")
        for row in rows:
            expectedResult = float(row["Result"])
            y = float(row["Value 1"])
            x = float(row["Value 2"])
            self.assertEqual(self.calculator.subtract(x, y), expectedResult)

    def testDivision(self):
        self.assertRaises(ZeroDivisionError, self.calculator.divide, 1, 0)
        rows = readCSV("tests/testCases/Division.csv")
        for row in rows:
            expectedResult = float(row["Result"])
            y = float(row["Value 1"])
            x = float(row["Value 2"])
            self.assertAlmostEqual(self.calculator.divide(x, y), expectedResult)

    def testMultiplication(self):
        rows = readCSV("tests/testCases/Multiplication.csv")
        for row in rows:
            expectedResult = float(row["Result"])
            x = float(row["Value 1"])
            y = float(row["Value 2"])
            self.assertAlmostEqual(self.calculator.multiply(x, y), expectedResult)

    def testSquare(self):
        rows = readCSV("tests/testCases/Square.csv")
        for row in rows:
            expectedResult = float(row["Result"])
            x = float(row["Value 1"])
            self.assertAlmostEqual(self.calculator.square(x), expectedResult)

    def testSquareRoot(self):
        rows = readCSV("tests/testCases/SquareRoot.csv")
        for row in rows:
            expectedResult = float(row["Result"])
            x = float(row["Value 1"])
            self.assertAlmostEqual(self.calculator.squareRoot(x), expectedResult)

    def testResultProperty(self):
        self.calculator.results.clear()
        self.assertEqual(self.calculator.results, [])


if __name__ == "__main__":
    unittest.main()


def build_test_suite():
    # create unittest.TestSuite object.
    test_suite = unittest.TestSuite()
    # add each test function to the test suite object.
    test_suite.addTest(TestCalculator('test_addition'))
    test_suite.addTest(TestCalculator('test_subtraction'))
    test_suite.addTest(TestCalculator('test_multiplication'))
    test_suite.addTest(TestCalculator('test_division'))
    test_suite.addTest(TestCalculator('test_squareRoot'))
    test_suite.addTest(TestCalculator('test_squared'))
    return test_suite
