from src.operations.add import add
from src.operations.divide import divide
from src.operations.subtract import subtract


class DescriptiveStatisticsOperations:
    @staticmethod
    def mean(numbers: list) -> float:
        summation = 0.0
        for number in numbers:
            add(summation, number)
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


