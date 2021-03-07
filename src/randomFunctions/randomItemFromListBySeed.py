import random
from src.randomFunctions.randomItemFromList import randomItemFromList


class randomItemsFromList(randomItemFromList):
    def __init__(self, array, seed):
        super().__init__(array)
        self.genItems = []
        random.seed(seed)
        super().generateChoice()
