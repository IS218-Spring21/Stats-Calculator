from src.allOperations.population_sampling_operations import PopulationSamplingOperations
from src.calculator import Calculator


class Population_Sampling_Calculator(Calculator):

    def __init__(self):
        Calculator.__init__(self)

    def random_sampling(self, input_list, new_list_length):
        self.results.append(PopulationSamplingOperations.sample_list(input_list, new_list_length))
        return self.results[-1]

    def confidence_interval_for_sample(self, confidence, sample_list):
        self.results.append(PopulationSamplingOperations.confidence_interval_sample(confidence, sample_list))
        return self.results[-1]

    def margin_error(self, input_list):
        self.results.append(PopulationSamplingOperations.margin_error(input_list))
        return self.results[-1]

    def sample_size(self, input_list):
        self.results.append(PopulationSamplingOperations.sample_size(input_list))
        return self.results[-1]

    def cochrans(self, input_list):
        self.results.append(PopulationSamplingOperations.cochrans(input_list))
        return self.results[-1]
