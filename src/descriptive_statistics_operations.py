from src.operations.add import add
from src.operations.divide import divide
from src.operations.power import power
from src.operations.root import root
from src.operations.subtract import subtract


class DescriptiveStatisticsOperations:
    @staticmethod
    def mean(numbers: list) -> float:
        summation = 0.0
        for number in numbers:
            summation = add(summation, number)
        return divide(summation, len(numbers))

    @staticmethod
    def median(numbers: list) -> float:
        numbers = sorted(numbers)
        if len(numbers) % 2 == 1:
            middleIndex = int(divide(len(numbers) - 1, 2))
            median = numbers[middleIndex]
        else:
            leftMiddleIndex = int(subtract(divide(len(numbers) - 1, 2), 0.5))
            rightMiddleIndex = int(add(divide(len(numbers) - 1, 2), 0.5))
            median = divide(add(numbers[leftMiddleIndex], numbers[rightMiddleIndex]), 2)
        return float(median)

    @staticmethod
    def mode(numbers: list) -> float:
        dictionary = {}
        for number in numbers:
            if number in dictionary.keys():
                dictionary[number] += 1
            else:
                dictionary[number] = 1
        mode = 0
        for number in dictionary.keys():
            if dictionary[number] > mode:
                mode = number
        return float(mode)

    @staticmethod
    def variance(numbers: list) -> float:
        mean = DescriptiveStatisticsOperations.mean(numbers)
        squaredDifferences = []
        for number in numbers:
            squaredDifferences.append(power(subtract(mean, number), 2))
        variance = divide(sum(squaredDifferences), subtract(len(numbers), 1))
        return variance

    @staticmethod
    def standardDeviation(numbers: list) -> float:
        standardDeviation = root(DescriptiveStatisticsOperations.variance(numbers), 2)
        return standardDeviation

