# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 03:27:11 2020

@author: Kedar
"""
import numpy as np
import matplotlib as plt
from scipy.optimize import curve_fit
from scipy.special import factorial
from scipy.stats import poisson
# get poisson deviated random numbers


# the bins should be of integer width, because poisson is an integer distribution
a=[184,
177,
190,
194,
176,
174,
198,
187,
158,
211,
189,
211,
172,
176,
209,
163,
190,
218,
163,
167]
a=a-150
s= np.std(a, ddof=1)
m=np.mean(a)
plt.figure
bins= np.arange(150,220,10)-0.5
entries, bin_edges, patches = plt.pyplot.hist(a, bins=bins, density=True, label='Frequency of number of decays')
plt.pyplot.title('Polonium decay frequency in 10 second periods')
plt.pyplot.xlabel('Decay Events')
plt.pyplot.ylabel('Frequency')

# calculate bin centres
bin_middles = 0.5 * (bin_edges[1:] + bin_edges[:-1])


def fit_function(k, lamb):
    '''poisson function, parameter lamb is the fit parameter'''
    return poisson.pmf(k, lamb)


# fit with curve_fit
parameters, cov_matrix = curve_fit(fit_function, bin_middles, entries)

# plot poisson-deviation with fitted parameter
x_plot = np.arange(150, 220,10)

plt.pyplot.plot(
    x_plot,
    fit_function(x_plot, *parameters),
    marker='o', linestyle='',
    label='Fit result',
)

plt.pyplot.legend()
plt.pyplot.savefig("1.png")


