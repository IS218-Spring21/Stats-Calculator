import unittest
from src.randomGenerator import RandomGenerators

class MyTestCase(unittest.TestCase):
    def test_random_number(self):
        print("*"*10+"Random Number Test"+"*"*10)
        print("Random Number: ")
        print(RandomGenerators.randNum(0,100))
    def test_random_number_by_seed_float(self):
        print("*" * 10 + "Random Float Number By Seed Test" + "*" * 10)
        #print(RandomGenerators.randInt(0, 100, 2))
        startVal = 0.0
        endVal = 100.0
        seed = 10
        print("Testing Random Numbers by seed:", seed)
        randomFloat = RandomGenerators.randNumBySeed(startVal, endVal, seed)
        print(randomFloat, RandomGenerators.randNumBySeed(startVal, endVal, seed))
        self.assertEqual(randomFloat, RandomGenerators.randNumBySeed(startVal, endVal, seed))

    def test_random_number_by_seed_int(self):
        print("*" * 10 + "Random Int Number By Seed Test" + "*" * 10)
        #print(RandomGenerators.randInt(0, 100, 2))
        startVal = 0
        endVal = 100
        seed = 3
        print("Testing Random Numbers by seed:", seed)
        randomInt = RandomGenerators.randNumBySeed(startVal, endVal, seed)
        print(randomInt, RandomGenerators.randNumBySeed(startVal, endVal, seed))
        self.assertEqual(randomInt, RandomGenerators.randNumBySeed(startVal, endVal, seed))





if __name__ == '__main__':
    unittest.main()
