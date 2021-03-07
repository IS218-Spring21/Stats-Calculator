import random
from src.randomFunctions.randomNumber import randNum


class randNumBySeed(randNum):
    def __init__(self, start, end, seed):
        super().__init__(start, end)
        random.seed(seed)
        super(randNumBySeed, self).generateValue()
