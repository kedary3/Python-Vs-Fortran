# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 14:30:43 2021

@author: Kedar
"""

from scipy.integrate import odeint
from scipy.optimize import brentq
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot,xlabel,ylabel,legend,show, figure, subplot


#define constants
xblock = 2000 #SECOND CAR IS 2000 M AHEAD
vblock = 3 #SECOND CAR IS MOVING AT 18 M/2
gamma = 4
T = 1.8
s_naught = 2.0
v_naught = 28
a = 0.7
b = 2
L = 5
 
xinit = 100 #100 M ALONG
vinit = 25 # 25 M/S START

# set the time interval for solving
Tstart = 0
Tend = 400 

def s_prime(v,delta_V):
    return s_naught + v*T+(v*delta_V/(2*np.sqrt(a*b)))

def rate_func( t, V ):
    # RATE_FUNC: IDM Car model
    # Model a car approaching a solid wall
    
    # unpack
    
    x = V[0] # position
    v = V[1] # velocity
    
    # Compute acceleration from IDM
    s = xblock+vblock*t - L - x
    delta_V = v - vblock
    a_idm = a*(1-(v/v_naught)**gamma-(s_prime(v,delta_V)/s)**2)
          
    # compute derivatives
    dx = v
    dv = a_idm
    
    # pack rate array
    rate = np.array([dx, dv])
    return rate
# Form Time array
time = np.linspace(Tstart,Tend,400) # 400 steps for nice plot
#pack constants
V0 = np.array([xinit,vinit])

Sol = odeint(rate_func, V0, time, tfirst=True)

# unpack the results. In the output array, variables are columns, times are rows
xout = Sol[:,0]
vout = Sol[:,1]


#graph
from matplotlib.pyplot import figure, subplot, title
fig=figure()

ax1 = subplot()
ax1.plot(time,xout,'b')
ax1.set_xlabel('time (s)')
ax1.set_ylabel('distance (m)', color='b')
ax1.tick_params('y', colors='b')

ax2=ax1.twinx()
ax2.plot(time,vout,'r')
ax2.set_ylabel('velocity (m/s)', color='r')
ax2.tick_params('y', colors='r')

fig.tight_layout()
title("Displacement and Velocity of Trailing Car Versus Time")
