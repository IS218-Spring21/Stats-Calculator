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

    def test_random_number_list_int_by_seed(self):
        print("*" * 10 + "Random Number List By Seed Test" + "*" * 10)
        startVal = 0
        endVal = 50
        seed = RandomGenerators.randNum(0, 10)
        listSize = 12
        print("Testing Random Numbers by seed:", seed)
        randomListInt = RandomGenerators.ranNumBySeedList(startVal, endVal, seed, listSize)
        print(randomListInt, RandomGenerators.ranNumBySeedList(startVal, endVal, seed, listSize))
        self.assertEqual(randomListInt, RandomGenerators.ranNumBySeedList(startVal, endVal, seed, listSize))




if __name__ == '__main__':
    unittest.main()
