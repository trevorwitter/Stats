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

def histogram(x):  #basic histogram plot for 1D array
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

def Normality(x):
    w,p = scipy.stats.shapiro(x)
    if p > .05:
        return "normal"
    else:
        return "not normal"

def norm_histo(x):
    if Normality(x) == "normal":
        print" normal distribution"
        print cohort_stats(x)
        return histogram(x)   
    else:
        print "not normal distribution"
        print cohort_stats(x)
        return histogram(x)

#2D Stats 
def de_mean(x):
    x_bar = np.mean(x)
    return [x_i - x_bar for x_i in x]

def variance(x):
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations)/(n-1)
     
def covariance(x, y):
    n = len(x)
    return np.dot(de_mean(x), de_mean(y)) / (n-1)
    
def correlation_plot(x, y):
    plt.plot(x, y, linestyle=' ', marker='.', color='b') 
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    print "slope", slope
    print "intercept", intercept  
    plt.title(("slope = ", slope))
    bestfit = [(i*slope)+intercept for i in x] 
    plt.plot(x, bestfit, linestyle='--', color='k')
    plt.show()
