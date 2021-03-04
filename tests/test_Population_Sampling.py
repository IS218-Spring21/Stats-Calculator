import unittest
import random
from numpy.random import randint

from src.population_sampling_calculator import Population_Sampling_Calculator

seedNum = 50

def random_list():
    random.seed(seedNum)
    original_list = []
    #original_list = randint(0, 50, 15)
    #return original_list
    # DONT CHNAGE THE 50 cause then everything has to change
    for x in range(50):
        original_list.append(float(random.randint(40, 50)))
    return original_list

class SamplingTestCase(unittest.TestCase):
    #original_list = []
    #seedNum = 0
    '''
    def setUp(self) -> None:
        random.seed(5)
        print("j")
        self.seedNum = 5
        self.original_list = randint(0, 50, 15)

        for x in range(10):
            self.original_list.append(float(random.randint(30, 50)))'''

    def test_random_sampling(self):
        print("******test_random_sampling******")
        original_list = random_list()
        sample_list = Population_Sampling_Calculator.random_sampling(original_list, 8, seedNum)
        print("Random Sample List")
        print(sample_list,"\n")
        self.assertEqual(sample_list, [41.0, 50.0, 47.0, 43.0, 42.0, 49.0, 47.0, 43.0])


    def test_confidence_interval_for_sample(self):
        print("******test_random_sampling******")
        original_list = random_list()
        sample_list = Population_Sampling_Calculator.random_sampling(original_list, len(original_list), seedNum)
        result = Population_Sampling_Calculator.confidence_interval_for_sample(0.9, sample_list)
        print("Confidence Interval for Sample List")
        print(result,"\n")
        self.assertAlmostEqual(result, (44.43924576646906, 45.840754233530944))

    def test_margin_error(self):
        print("******test_margin_error******")
        original_list = random_list()
        res = Population_Sampling_Calculator.margin_error(original_list)
        print("Margin of Error:", res, "\n")
        self.assertEqual(res, 0.41797373220852824)


if __name__ == '__main__':
    unittest.main()
