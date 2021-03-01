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

