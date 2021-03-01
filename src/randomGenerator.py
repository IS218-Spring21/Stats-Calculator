import random

class RandomGenerators:
    # Generate a random number without a seed between a range of two numbers - Both Integer and Decimal
    @staticmethod
    def randNum (start, end):
        #If type of start and end is int
        if (type(start) is int) & (type(end) is int):
            return random.randint(start, end)
        #If type of start and end is float
        if (type(start) is float) & (type(end) is float):
            return random.uniform(start, end)
        else:
            return "ERROR: Both value are either not the same type or wrong type in general"

    # Generate a random number with a seed between a range of two numbers - Both Integer and Decimal
    @staticmethod
    def randNumBySeed (start, end, seed):
        random.seed(seed)
        return RandomGenerators.randNum(start, end)

    # Generate a list of N random numbers with a seed and between a range of numbers - Both Integer and Decimal
    @staticmethod
    def ranNumBySeedList (start, end, seed, n):
        isInt = False
        if (type(start) is int) & (type(end) is int):
            isInt = True
        elif (type(start) is float) & (type(end) is float):
            isInt = False
        else:
            return "ERROR: Both value are either not the same type or wrong type in general"

        random.seed(seed)
        list = [None] * n
        for i in range(n):
            if isInt:
                list[i] = random.randint(start, end)
            else:
                list[i] = random.uniform(start, end)
            # list[i] = RandomGenerators.randNumBySeed(start,end,seed)
        return list

        # return [random.randint(start, end)] * n

    # Select a random item from a list
    @staticmethod
    def randItemFromList(array):
        if isinstance(array, list):
            return array[RandomGenerators.randNum(0, len(array)-1)]
        else:
            return "ERROR: Variable not Array"

    # Set a seed and randomly select the same value from a list
    @staticmethod
    def randItemFromListBySeed(array, seed):
        random.seed(seed)
        return RandomGenerators.randItemFromList(array)

