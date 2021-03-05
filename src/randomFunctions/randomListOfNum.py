from src.randomFunctions.randomNumberBySeed import randNum


class randListOfNum(randNum):
    def __init__(self, start, end, n):
        super().__init__(start, end)
        self.n = n
        self.genList = []
        self.generateList()

    def generateList(self):
        for i in range(self.n):
            super().generateValue()
            self.genList.append(super().getResult())

    def getResult(self):
        return self.genList
