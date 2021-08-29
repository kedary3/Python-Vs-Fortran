# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 14:58:50 2021

@author: Kedar
"""

from scipy.optimize import brentq
from scipy.integrate import odeint
import numpy as np

#define constants

T_room = 20
T_pref = 60
T_hot = 90
r=0.001
t0=90
hV = 8
cV = 1
ctemp=20    

#define initial conditions
L0 = np.array([t0])
def newton_Temp(t,V):
      
    y = V[0]    
        
    
    dy =  -r*(y-T_room)
    
    
    # pack rates into numpy arrray
    rate = np.array([dy])
    return rate

import matplotlib.pyplot as plt
from matplotlib.pyplot import plot,xlabel,ylabel,legend,show, figure, subplot

#plot temperature of passive cooling over time
time = np.linspace(0,3600,600)
T_time = odeint(newton_Temp, L0, time , tfirst = True)

plt.plot(time,T_time)
plt.show()

#define the temperature of a mixture given intial temp and respective volumes
def mix_func(v1,t1,v2,t2):
    # Calculates the final temperature of two liquids after they have been
    # mixed based upon the initial temperature and volume of each individual liquid.
    # Function is passed:
    # V1, initial Volume of liquid one
    # T1, initial temperature of liquid one
    # V2, initial Volume of liquid two
    # T2, initial temperature of liquid two
    # Tmix, the temperature of the mixture

    Tmix = (v1*t1 + v2*t2)/(v1 + v2)
    return Tmix

def CoffeeTemp(t):
    # This function returns the temperature of the coffee after cooling
    # for t seconds and mixing with cream. It models the physical
    # process in the problem, first cooling then mixing.

    # first let the coffee cool for t seconds
    TT = odeint(newton_Temp,L0,[0,t], tfirst = True)

    # second mix cream with coffee to get final temperature
    hctemp = TT[-1]

    Temp = mix_func(hV, hctemp, cV, ctemp)

    return Temp


def coffee_Error(t):
    return CoffeeTemp(t)-T_pref

minutes = brentq(coffee_Error,10,3600)/60
print("you should mix your cream into your coffee after", np.round(minutes,3), "minutes")


