from pandas import DataFrame, groupby
import pandas as pd
import numpy as np
import scipy.stats
from scipy.stats import linregress
from random import random
import matplotlib.pyplot as plt
from collections import Counter

df = pd.read_excel('/Users/twitter/Desktop/R1_baseline2.xlsx')
frame = DataFrame(df)

#1D stats 
def cohort_stats(x):
    mean = np.mean(x)
    stdev = np.std(x)
    max_value = np.max(x)
    min_value = np.min(x)
    stats = {'mean':mean, 'stdev':stdev, 'max':max_value, 'min':min_value}
    return stats
