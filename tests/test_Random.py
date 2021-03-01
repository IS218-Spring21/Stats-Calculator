import unittest
from src.randomGenerator import RandomGenerators

class MyTestCase(unittest.TestCase):
    def test_random_number(self):
        print("*"*10+"Random Number Test"+"*"*10)
        print("Random Number: ")
        print(RandomGenerators.randNum(0,100))




if __name__ == '__main__':
    unittest.main()
