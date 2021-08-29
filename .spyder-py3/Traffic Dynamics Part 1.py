# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 20:41:56 2021

@author: Kedar
"""

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



#define default constants
v_naught = 28
T = 1.8
s_naught = 2.0
a = 3
b = 3
L = 5
delta = 4
 

# set the time interval for solving
Tstart = 0
Tend = 20

# define number of cars in a line
# define car array

cars = 5

cars_init = np.zeros_like(1,shape=(cars,7),dtype= float)
default_init = [v_naught,T,s_naught,a,b,L,delta]
for i in range(np.size(default_init)):
    for k in range(cars):
        cars_init[k][i]= default_init[i]


init = np.zeros(2*cars)
for i in range(2*cars):
    if i<cars:
        # init[i] = i*L*A
         init[i] = (10)*(-i)  #-20*np.random.uniform(0,1)) #initial positions
    else:
         init[i] = 0 #+20*np.rint(np.random.uniform(0,1)) #initialize velocities



def s_prime(v,delta_V):
    return s_naught + v*T+(v*delta_V/(2*np.sqrt(a*b)))

def rate_func( t, V, cars_init ):
    # RATE_FUNC: IDM Car model
    # Model a car approaching a solid wall
    
    # unpack
    
    x = V[:cars] # position
    v = V[cars:] # velocity
    
    
    dv = np.zeros(2*cars)
    
    for i in range(cars):
        #unpack driver properties
        v_naught = cars_init[i][0] 
        T = cars_init[i][1]
        s_naught = cars_init[i][2]
        a = cars_init[i][3]
        b = cars_init[i][4]
        L = cars_init[i][5]
        delta = cars_init[i][6]
        if(i == 0): #front car
            a_idm = a*(1-(v[i]/v_naught)**delta)
            dv[cars+i] = a_idm
        else:
            # Compute acceleration from IDM
            s = (x[i-1] - L - x[i])
            delta_V = v[i] - v[i-1]
            a_idm = a*(1-(v[i]/v_naught)**delta-(s_prime(v[i],delta_V)/s)**2)
            dv[cars+i] = a_idm     
        # compute derivatives
        dx = v
        dv[:cars] = dx
    
    # pack rate array
    rate = dv
    return rate

def model(cars_init,init):
    # Form Time array
    time = np.linspace(Tstart,Tend,100) # 15mins for nice plot
    #pack constants
     
    
    
    Sol = odeint(rate_func, init, time, args=(cars_init,), tfirst=True)
    
    # unpack the results. In the output array, variables are columns, times are rows
    xout = Sol[:,:cars]
    vout = Sol[:,cars:]
    
    
    #graph
    from matplotlib.pyplot import figure, subplot, title
    fig=figure()
    
    from random import randint
    colors = []
    
    for i in range(cars):
        colors.append('#%06X' % randint(0, 0xFFFFFF))
    ax1 = subplot()
    ax2=ax1.twinx()
    for car in range(cars):
        ax1.plot(time,xout[:,car],colors[car])
        ax2.plot(time,vout[:,car],colors[car])
        print((vout[-1,car]-vout[0,car])/(Tend-Tstart)) #find average avveleration after 20 seconds
    fig.tight_layout()
    title("Displacement and Velocity of Line of Cars Versus Time")
    ax1.set_ylabel('distance (m)', color='b')
    ax1.tick_params('y', colors='b')
    ax1.set_xlabel('time (s)')
    ax2.set_ylabel('velocity (m/s)', color='r')
    ax2.tick_params('y', colors='r')



#execute

model(cars_init,init) #default parameters model


"""
give initial condition where one driver is not the same as the others
"""
#define default constants
v_naught = 28
T = 1.8
s_naught = 2.0
a = 3
b = 3
L = 5
delta = 4
 

# set the time interval for solving
Tstart = 0
Tend = 1.25


# define number of cars in a line
# define car array

cars = 5

cars_init = np.zeros_like(1,shape=(cars,7),dtype= float)
default_init = [v_naught,T,s_naught,a,b,L,delta]
non_default_init = [v_naught, 5, 3*s_naught, 0.24, 0.51, 3*L,4]
for i in range(np.size(default_init)):
    for k in range(cars):
        # if (k == 3 ): #rogue car is in fourth position in line
        #     cars_init[k][i]= non_default_init[i]
        # else:
            cars_init[k][i]= default_init[i]
        

init = np.zeros(2*cars)
for i in range(2*cars):
    if i<cars:
        if i ==0:
            init[0] = 0
        else:
            init[i] = -3*(L*i)#-(cars_init[i][2]+cars_init[i][5]))  #-20*np.random.uniform(0,1)) #initial positions
        print(init[i])
    else:
        if (i==cars): #set first car still
        
            init[i] = 0
        else:
            init[i] = 20  #initialize velocities

#execute
model(cars_init,init)



