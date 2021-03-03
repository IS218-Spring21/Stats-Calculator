import random


# Takes a list as input and return a new list with a sample of the original list
def sample_list(input_list, new_list_length):
    if not input_list:
        return "Error: input list was empty"
    if new_list_length > len(input_list):
        return "Error: sample list length is bigger than original list"
    return random.sample(input_list, new_list_length)
