# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 14:06:10 2021

@author: Kedar
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 13:11:41 2019

@author: esalathe

Example of a coupled system of ODEs to model the population dynamics of a
preditor-prey system (foxes and rabbits)
"""

import matplotlib.pyplot as plt
from scipy.integrate import odeint
from numpy import linspace,array,zeros,log,exp,sin,cos,sqrt,pi,e
from matplotlib.pyplot import plot,xlabel,ylabel,legend,show, figure, subplot

#define lorenz constants
sigma = 10 
beta = 8/3 
rho = 28

#define set of lernz differential eqs
def Lorenz(t,V):
    
    #provide initial conditions as array
    x = V[0]
    y = V[1]
    z = V[2]
        
    #lorenz eqs    
    dx = -sigma*x+sigma*y
    dy = rho*x-y-x*z
    dz = -beta*z+x*y
    
    # pack rates into numpy arrray
    rate = array([dx, dy, dz])
    return rate

def lotka(t, V):
# Poulation growth of Rabbits and Foxes
# Note that rabbits is first column, foxes second

# unpack
    r = V[0]
    f = V[1]
        
    # compute rates
    dr = a*r - b*r*f
    df = e*b*r*f - c*f
        
    # pack rates into numpy arrray
    rate = array([dr, df])
    return rate

# set some parameters
a= 0.1
b= 0.01
c= 0.1
e= 0.2

# set initial conditions
rabbit0 = 100
fox0 = 10
#lorenz init
x0=1
y0=2
z0=3

#fox init
Y0 = array([rabbit0, fox0]) # pack the i.c. into a numoy array
#lorenz init
L0 = array([x0, y0,z0])
# set the time interval for solving
Tstart=0
Tend = 10 

# Form Time array

T = linspace(Tstart,Tend,500)

# solve the ODE
X = odeint(Lorenz, L0, T, tfirst=True)

# unpack the results. In the output array, variables are columns, times are rows
# rabbits = X[:,0]
# foxes = X[:,1]

# make some nice plots
# figure

#unpack the results
x = X[:,0]
y = X[:,1]
z = X[:,2]
# subplot(2,1,1)
# plot (T,rabbits, label='Rabbits')
# plot (T,foxes, label='Foxes')
# xlabel('Day')
# ylabel('Population')
# legend()

# subplot(2,1,2)
# plot (rabbits,foxes)
# xlabel('Rabbits')
# ylabel('Foxes')

#3d plot attractor
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(x, y, z)
plt.show()


