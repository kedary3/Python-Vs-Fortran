# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 23:11:18 2021

@author: Kedar
"""


from scipy.integrate import odeint
from scipy.optimize import brentq
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot,xlabel,ylabel,legend,show, figure, subplot

# define constants
D0=1
DMAX=D0*1.1
DMIN=1
H0=[2]
d=0.02
h1=0.05
g=9.81


#define bulge in tank
def Diameter(h):
    return D0*(1+.1*np.sin(np.pi/H0[0]*h))

# graph diameter
x=np.linspace(0,H0)
D=Diameter(x)
fig, (ax1, ax2) = plt.subplots(2)
ax1.plot(x,D)

#define height
def height(t):
    sol = odeint(rate, H0, [0,t], tfirst=True)
    
    sol1= sol[:,0]
    return sol1

# # define height difference
def height_diff(t):
    return height(t)[1]-h1
    
#define rate of chnage of height
def rate(t,H):
    
    h=H[0]
    dh=-np.sqrt(2*g)*(d**2/(Diameter(h))**2)*np.sqrt(h)
    #pack results
    rate = np.array([dh])
    return rate

#graph rate
# x=np.linspace(0,2000)
# D=rate(x,H0)[0,:]
# ax2.plot(x,D)

# def height_diff(t):
#rearrange eqn 2
def t_analytic(D,h):
    return (np.sqrt(h)-np.sqrt(H0))/(-np.sqrt(g/2)*(d/D)**2)
    
#print brentq brackets
low_t = t_analytic(DMIN,0.05)
high_t = t_analytic(DMAX,0.05)
print(low_t)
print(high_t)

#find optimal time
print(height_diff(low_t))
print(height_diff(high_t))
print("the bulging tank will reach a water height of ",h1, "meters")
print("after", np.round(brentq(height_diff,low_t,high_t)/60,2), "minutes")


