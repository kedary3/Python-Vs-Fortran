#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 12:05:58 2020

@author: esalathe
"""
import numpy as np

from numpy import (linspace,log,exp,sin,cos,sqrt,pi,e, 
                   arange, zeros_like, ones, eye, diagflat, matmul, argsort)
from numpy.linalg import eig
from scipy.sparse import diags

# Parameters 
a=1.e-11 # m size of electron
hbar=197*1e-9 # hbar-c
m=0.511*1e6 # eV/c2

L = 20*a# length of domain -10a<x<10a
N = 1000 # number of grid cells
dx = L/N# size of grid cell

# set the x interval for solving, 10 electron radii each direction: -10a < x < 10a 
x =  np.linspace(-L/2,L/2,N)# x runs -L/2 to +L/2 by steps dx

# Define the potential well 
# either zero for square well or like above for quadratic well 
V0 = 50
Vpot = V0*x**2/a**2

# Form the matrix
n = N
k = np.array([np.ones(n-1),-2*np.ones(n),np.ones(n-1)])
offset = [-1,0,1]
Tdiag = diags(k,offset).toarray()
H = (-hbar/2*m)*Tdiag+Vpot

# Get eigenvalues and eigenvectors
w,v = eig(H)

# sort by magnitude of eig vals, selecting just lowest 3 energy levels
idx=argsort(w)
E = w[idx[:3]]
Psi = v[:,idx[:3]]

# plot lowest 3 energy levels
from matplotlib.pyplot import plot,xlabel,ylabel,legend,show, figure, subplot 
for i in range(3):
    plot(x,Psi[:,i], label='E='+str(round(E[i],9)))
legend() 