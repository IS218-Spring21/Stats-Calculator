from src.randomFunctions.randomNumberBySeed import randNumBySeed


class randListOfNum(randNumBySeed):
    def __init__(self, start, end, n, seed):
        super().__init__(start, end, seed)
        self.n = n
        self.genList = []
        self.generateList()

    def generateList(self):
        for i in range(self.n):
            super().generateValue()
            self.genList.append(super().getResult())

    def getResult(self):
        return self.genList
