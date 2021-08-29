# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 20:29:45 2021

@author: Kedar
"""

from numpy import linspace,array,arange, log,exp,sin,cos,sqrt, pi, zeros, ones
import numpy as np
from numpy.linalg import eig
from matplotlib.pyplot import plot,xlabel,ylabel,legend,show, figure, subplot, title, tight_layout, stem

#  set the time array
T = 10
dt = 0.01

# 1) Fill in t array using arange
t = arange(0,T,dt)

# 2) Create the Matrix M and find the eigenvalues and eigenvectors
k1 = 1
k2 = 1

beta = k1 + k2
alpha = k2
M = [[-beta,alpha],[alpha,-beta]]

# 3) use eig(M) to store eigen values in array w and eigen vectors in matrix v

w , v = eig(M)



# 4) Create the time series of the motion of each mass as cosines 
#     for the first eigenvalue/eigenvector
#  What is omega for the selected mode?
#  What is v1 and v2?

imode=0

omega = np.sqrt(-w)
v1 = v[0,imode]
v2 = v[1,imode]

x1 = v1*cos(omega[imode]*t)
x2 = v2*cos(omega[imode]*t)

# plot(t,x1, t,x2)

#5 Now superpose a mix of both eigen values, 0.5 each. Plot the motion of the two masses. 
#   What would the initial conditions be to get that mix?


x1 = 1/2*(v[0,imode]*cos(omega[imode]*t) + v[0,imode+1]*sin(omega[imode+1]*t))
x2 = 1/2*(v[1,imode]*cos(omega[imode]*t) + v[1,imode+1]*sin(omega[imode+1]*t))
plot(t,x1, t,x2)