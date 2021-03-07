import random
from src.randomFunctions.randomItemsFromList import randomItemsFromList


class randomItemsFromListBySeed(randomItemsFromList):
    def __init__(self, array, n, seed):
        super().__init__(array, n)
        self.seed = seed
        random.seed(self.seed)
        super().generateChoices()
