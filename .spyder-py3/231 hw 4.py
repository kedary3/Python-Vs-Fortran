# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 20:29:51 2020

@author: Kedar
"""
import numpy as np

def weightedAverage(x,s):
    print(np.shape(s))
    w=[0,0]
    for i in range(np.shape(s)[0]):
        w[i]=1/(s[i]**2)
    xwav=0
    for i in range(np.shape(x)[0]):
        xwav += w[i]*x[i]
    wavsum =0
    for i in range(np.shape(x)[0]):
        wavsum+=w[i]
    xwav=xwav/(wavsum)
    sigmaError=1/np.sqrt(wavsum)
    print(xwav)
    print(sigmaError)
weightedAverage([103,96],[5,4])