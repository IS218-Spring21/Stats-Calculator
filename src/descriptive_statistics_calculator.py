from src.allOperations.descriptive_statistics_operations import DescriptiveStatisticsOperations
from src.calculator import Calculator


class DescriptiveStatisticsCalculator(Calculator):

    def __init__(self):
        Calculator.__init__(self)

    def mean(self, input_list: list) -> float:
        self.results.append(DescriptiveStatisticsOperations.mean(input_list))
        return self.results[-1]

    def median(self, input_list: list) -> float:
        self.results.append(DescriptiveStatisticsOperations.median(input_list))
        return self.results[-1]

    def modes(self, input_list: list) -> list:
        self.results.append(DescriptiveStatisticsOperations.modes(input_list))
        return self.results[-1]

    def variance(self, input_list: list) -> float:
        self.results.append(DescriptiveStatisticsOperations.variance(input_list))
        return self.results[-1]

    def standardDeviation(self, input_list: list) -> float:
        self.results.append(DescriptiveStatisticsOperations.standardDeviation(input_list))
        return self.results[-1]

    def zScores(self, input_list: list) -> list:
        self.results.append(DescriptiveStatisticsOperations.zScore(input_list))
        return self.results[-1]
