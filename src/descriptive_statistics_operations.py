from src.operations.add import add
from src.operations.divide import divide


class DescriptiveStatisticsOperations:
    @staticmethod
    def mean(numbers: list) -> float:
        summation = 0.0
        for number in numbers:
            add(summation, number)
        return divide(summation, len(numbers))
