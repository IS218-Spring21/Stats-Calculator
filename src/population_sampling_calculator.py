from src.population_sampling_functions import random_sampling
from src.population_sampling_functions import confidence_interval_for_sample
from src.population_sampling_functions import margin_error

class Population_Sampling_Calculator:
    list = []

    def __init__(self):
        self.list = []

    @staticmethod
    def random_sampling(input_list, new_list_length, seedNum):
        return random_sampling.sample_list(input_list, new_list_length, seedNum)

    @staticmethod
    def confidence_interval_for_sample(confidence, sample_list):
        return confidence_interval_for_sample.confidence_interval_sample(confidence, sample_list)

    @staticmethod
    def margin_error(input_list):
        return margin_error.margin_error(input_list)


