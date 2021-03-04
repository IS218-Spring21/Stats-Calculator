from scipy.stats import sem, t
import numpy as np


def confidence_interval_sample(confidence, sample_list):
    n = len(sample_list)
    avg = np.mean(sample_list)
    std_err = sem(sample_list)
    interval = std_err * t.ppf((1 + confidence) / 2, n - 1)
    low = avg - interval
    high = avg + interval
    return low, high
