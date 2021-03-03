import spicy
from spicy import stats
import random_sampling


def confidence_interval_for_sample(confidence, input_list, sample_size):
    sample_list = random_sampling.sample_list(input_list, sample_size)
    n = len(sample_list)
    avg = spicy.mean(input_list)
    std_err = stats.sem(input_list)
    interval = std_err * stats.t.ppf((1+confidence) / 2, n-1)
    low = avg - interval
    high = avg + interval
    return low, high




