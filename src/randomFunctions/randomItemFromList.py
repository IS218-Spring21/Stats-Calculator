import random


class randomItemFromList:
    def __init__(self, array):
        self.array = array
        self.output = None
        random.seed()
        self.generateChoice()

    def generateChoice(self):
        if not isinstance(self.array, list):
            return "ERROR: Input not Array"
        else:
            self.output = random.choice(self.array)

    def getValue(self):
        return self.output
