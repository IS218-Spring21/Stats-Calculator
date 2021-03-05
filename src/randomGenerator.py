import random
from src.randomFunctions import randomItemFromList, randomItemFromListBySeed, randomItemsFromList, randomItemsFromListBySeed, randomListOfNum, randomNumber, randomNumberBySeed

class RandomGenerators:
    # Generate a random number without a seed between a range of two numbers - Both Integer and Decimal
    def randNum (self, start, end):
        return randomNumber.randNum(start, end).getResult()


    # Generate a random number with a seed between a range of two numbers - Both Integer and Decimal

    def randNumBySeed (self, start, end, seed):
        return randomNumberBySeed.randNumBySeed(start, end, seed).getResult()

    # Generate a list of N random numbers with a seed and between a range of numbers - Both Integer and Decimal

    def ranNumBySeedList (self, start, end, n, seed):
        return randomListOfNum.randListOfNum(start, end, n, seed).getResult()

    # Select a random item from a list

    def randItemFromList(self, array):
        return randomItemFromList.randomItemFromList(array).getValue()

    # Set a seed and randomly select the same value from a list

    def randItemFromListBySeed(self, array, seed):
        return randomItemFromListBySeed.randomItemsFromList(array, seed).getValue()

    # Select N number of items from a list without a seed

    def randItemsFromList(self, array, n):
        return randomItemsFromList.randomItemsFromList(array, n).getValue()

    # Select N number of items from a list with a seed

    def randItemsBySeedFromList(self, array, n, seed):
        return randomItemsFromListBySeed.randomItemsFromListBySeed(array, n, seed).getValue()