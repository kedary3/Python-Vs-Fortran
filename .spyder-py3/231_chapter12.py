# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 12:54:28 2020

@author: Kedar
"""
import numpy as np
import matplotlib.pyplot as plt
x=[731,772,771,681,722,688,653,757,733,742,739,780,709,676,760,748,672,687,766,645,678,748,689,810,805,778,764,753,709,675,698,770,754,830,725,710,738,638,787,712]
mn=np.mean(x)
std=np.std(x,ddof=1)
print(mn,std)

bins = [0, mn-2*std,mn-std, mn, mn+std, mn+2*std, np.inf]





def gaussian(x, mu, sig):
    return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))

x_values = np.linspace(0, 1000, 120)
for mu, sig in [(-1, 1), (0, 2), (2, 3)]:
    plt.plot(x_values, gaussian(x_values, mn, std))
    plt.hist(x, bins=bins,histtype='barstacked')
plt.show()
# We can set the number of bins with the `bins` kwarg

