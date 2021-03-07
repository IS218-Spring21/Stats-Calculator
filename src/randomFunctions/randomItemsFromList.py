from src.randomFunctions.randomItemFromList import randomItemFromList


class randomItemsFromList(randomItemFromList):
    def __init__(self, array, n):
        super().__init__(array)
        self.genItems = []
        self.n = n
        self.generateChoices()

    def generateChoices(self):
        if self.n > len(self.array):
            self.genItems = "ERROR: n is greater then array size"
        else:
            for i in range(self.n):
                super().generateChoice()
                # want to append randomly chosen value from
                # array and remove that value from the
                # list so we don't choose it again
                self.genItems.append(super().getValue())
                self.array.remove(super().getValue())

    def getValue(self):
        return self.genItems
