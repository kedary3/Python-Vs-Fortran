# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 22:59:50 2021

@author: Kedar
"""
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot,xlabel,ylabel,legend,show, figure, subplot

x0=0
y0=0
theta=np.pi/6
v_naught = 100
xdot0 = v_naught*np.cos(theta)
ydot0 = v_naught*np.sin(theta)

g = 9.81
R = 0.08
P = 1.22
C = 0.47
M = 1

V0=np.array([x0,y0,xdot0,ydot0])
def traj(x, V):
    # unpack
    x0 = V[0]
    y0 = V[1]
    dx0 = V[2]
    dy0 = V[3]
                
    # compute rates
    A = np.pi*(R**2)*P*C/(2*M)
    x_prime = dx0 
    y_prime = dy0
    xdot_prime = -A*x_prime*np.sqrt(x_prime**2+y_prime**2)
    ydot_prime = -g-A*y_prime*np.sqrt(y_prime**2+x_prime**2)
        
    # pack rates into column vector
    rate = np.array([x_prime,y_prime,xdot_prime,ydot_prime])
    return rate

x = np.linspace(0,7)
out = odeint(traj, V0, x, tfirst=True)
x_pos = out[:,0]
y_pos = out[:,1]
dx = out[:,2]
dy = out[:,3]
plt.plot(x[0:150],y_pos[0:150])
floor=np.arange(9)
plt.plot(np.arange(np.size(floor)),np.zeros_like(floor))
