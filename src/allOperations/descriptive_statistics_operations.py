from src.allOperations.basicOperations import BasicOperations


class DescriptiveStatisticsOperations:
    @staticmethod
    def mean(numbers: list) -> float:
        summation = 0.0
        for number in numbers:
            summation = BasicOperations.addition(summation, number)
        return BasicOperations.division(summation, len(numbers))

    @staticmethod
    def median(numbers: list) -> float:
        numbers = sorted(numbers)
        if len(numbers) % 2 == 1:
            middleIndex = int(BasicOperations.division(len(numbers) - 1, 2))
            median = numbers[middleIndex]
        else:
            leftMiddleIndex = int(BasicOperations.subtraction(BasicOperations.division(len(numbers) - 1, 2), 0.5))
            rightMiddleIndex = int(BasicOperations.addition(BasicOperations.division(len(numbers) - 1, 2), 0.5))
            median = BasicOperations.division(BasicOperations.addition(numbers[leftMiddleIndex], numbers[rightMiddleIndex]), 2)
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
            squaredDifferences.append(BasicOperations.square(BasicOperations.subtraction(mean, number)))
        variance = BasicOperations.division(sum(squaredDifferences), BasicOperations.subtraction(len(numbers), 1))
        return variance

    @staticmethod
    def standardDeviation(numbers: list) -> float:
        standardDeviation = BasicOperations.squareRoot(DescriptiveStatisticsOperations.variance(numbers))
        return standardDeviation

    @staticmethod
    def zScore(numbers: list) -> list:
        zScores = []
        standardDeviation = DescriptiveStatisticsOperations.standardDeviation(numbers)
        mean = DescriptiveStatisticsOperations.mean(numbers)
        for number in numbers:
            zScores.append(BasicOperations.division(BasicOperations.subtraction(number, mean), standardDeviation))
        return zScores
