# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 04:33:50 2020

@author: Kedar
"""

import numpy as np
import matplotlib.pyplot as plt
x=[63, 58 , 74, 78 , 70 , 74, 75, 82, 68, 69, 76,62, 72, 88 , 65, 81 ,79, 77, 66,76,86,72,79,77,60,70,65,69,73,77,72,79,65,66,70,74,84,76,80,69]
xb=np.mean(x)
std=np.std(x)
#print(xb,std)
#print(len(x))
tq=[0,0,0,0,0,0,0,0,0,0]
for i in range(10):
    t=[x[i],x[10+i],x[20+i],x[30+i]]
    print(np.mean(t),np.std(t,ddof=1))
    tq[i]=np.mean(t)   
print(tq)
print(np.std(tq))
n_bins = 10



fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)

# We can set the number of bins with the `bins` kwarg
axs[0].hist(x, bins=n_bins,rwidth=3.38)
axs[1].hist(tq, bins=n_bins,rwidth=3.38)