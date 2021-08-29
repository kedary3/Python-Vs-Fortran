# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 03:05:36 2021

@author: Kedar
"""
import numpy as np
from numpy import arange, zeros_like, ones, eye, diagflat, matmul
from scipy.sparse import diags
import numpy as np



# Solve Heat Equation numerically using a time and space mesh

from numpy import linspace,array, log,exp,sin,cos,sqrt, pi,e
import numpy as np
from numpy import zeros, diagflat, ones, eye, matmul
from matplotlib.pyplot import plot,xlabel,ylabel,legend,show,figure,title, pause
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

# Parameters for the problem 
K = 0.5 # heat conduction K = 0.5

# Spatial Grid
L = 15.  # Length of bar
dx = 0.1 # Spacing of points on bar
nx = int(150) # fill in

x = linspace(0,L,nx) # fill in

# Time grid
stopTime = 20 # Time to run the simulation
dt = .01 # Size of time step
nt = int(2000)  # fill in

time = linspace(0,stopTime,nt)  # fill in

# Create empty array to contain T(t,x)
T = zeros((nt,nx)) # nt times, nx positions

# Set the initial condition at t=0
T[0,:] = 50. # uniform initial state

# Boundary Condition at x[0] and x[-1]
Ta = 100. # left side
Tb = 0. # right side

# Create Matrix for iterating forward in time
#
n = nx
k = np.array([np.ones(n-1),-2*np.ones(n),np.ones(n-1)])
offset = [-1,0,1]
Tdiag = diags(k,offset).toarray()


M =  (eye(nx)+(K*dt/(dx)**2)*Tdiag)# fill in by using Tdiag, I, heat equation and matrix addition. Recall matmul(A,B) for matrix multiplication

# loop forward in time and compute change in string
for it in range(1,nt):  # fill in loop over it
    # Calculate the future temperature along the center of bar in matrix form. 
    # Note that boundary condition is reapplied at each time step
    
    T[it,:] = matmul(M,T[it-1,:]) # fill in matrices to multiply 
                        # (What is temperature at previous time?)
    
    # apply left side boundary condition
    T[it,0] = Ta # fixed temperature
    
    # apply right side boundary condition
    T[it,-1] = Tb # fixed temperature

# Make some plots

# Steady state?
figure(1)
plot(x, T[-1,:])
xlabel('Distance')
ylabel('Temperature')
title('Final State Solution')


# Animated graph for every 10th time step
figure(2)
for it in range(0,nt,20):
    plot(x, T[it,:])
    xlabel('Distance')
    ylabel('Temperature')
    title('Transient Solution')       
    pause(.00001)

# 3-D suface plot
    
fig = figure(3)
ax = fig.gca(projection='3d')

# make X, Y grids
X, Y = np.meshgrid(x,time)

# Plot the surface.
surf = ax.plot_surface(X, Y, T, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)
xlabel('Distance (cm)')
ylabel('Time (s)')


