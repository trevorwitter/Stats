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

def histogram(x):  #basic histogram plot for 1D array. Add test for normal distribution
    y = np.array(x)
    rounded = np.rint(y)
    subject_counts = Counter(rounded)
    xs = range(160)
    ys = [subject_counts[z] for z in xs]
    plt.bar(xs, ys)
    xmin = min(x)
    xmax = max(x)
    plt.xlim(xmin, xmax)
    ymax = (max(ys)*1.15)
    plt.ylim(0, ymax)
    plt.show()

