# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 14:26:35 2021

@author: Kedar
"""
import numpy as np
import matplotlib.pyplot as plt
#dy/dt=y(1-sin(wt)) = W(t,y): y(t=0)=1, w=4pi
y0=1
dt=.1
w=4*np.pi
#initialize time array
t = np.arange(0,1+dt,dt)

#define differential equation
def func(y,t):
    return y*(1-np.sin(w*t))

#define Euler Method
def euler(f,y0,t):
    from numpy import zeros_like, size

    
    # create array to hold the solution
    y = np.zeros_like(t)
    #initialize y
    y[0] = y0 
    # set i.c. ie fill the first value of soln array, y

    # use for loop to fill in the rest of the solution
    # hint: use size(t) to find number of values
    for i in range(1,size(t)):
       y[i] = y[i-1]+dt*func(y[i-1],t[i-1]) #euler method equation

    return y

#apply euler method to func
y_euler = euler(func,y0,t)
print(euler(func,y0,t))


#apply odeint method to func
from scipy.integrate import odeint
y_odeint = odeint(func,y0,t, tfirst=False)
print(y_odeint)


#plot approximations of differential solution 
fig = plt.figure()
plt.ylabel("value")
plt.xlabel("time")

plt.plot(t,y_euler,label="Euler Method")
plt.plot(t,y_odeint,label="Odeint Method")

#solve for A in solution using initial condition
#y(t)=-Ae^(cos(wt)/w+t)
#A=-e^-1/4pi

def func_sol(t,w):
    return np.e**(-1/w)*np.exp((np.cos(w*t)/w)+t)

#Plot analytical solution alongside approximations 
x=0.00001
time = np.arange(0,1+x,x)
plt.plot(time,func_sol(time,w),label="Solution")
plt.legend()
plt.show()