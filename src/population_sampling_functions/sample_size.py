from scipy import stats
from scipy.stats import sem, t
import numpy as np

def sample_size(input_list):
    # confidence = 0.05
    error = sem(input_list)
    std = stats.gstd(input_list)
    # z = stats.zscore(input_list)
    z = 1.96
    n = ((z*std)/error) ** 2
    return int(n)


