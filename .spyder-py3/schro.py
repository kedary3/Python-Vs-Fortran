# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 14:29:46 2021

@author: Kedar
"""

from scipy.optimize import brentq
from scipy.integrate import odeint
import scipy as sc
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot,xlabel,ylabel,legend,show, figure, subplot


#set initial conditions 
psi0 = 0
dpsi0 = 1

# pack array
V0 = np.array([psi0, dpsi0, ])

#set potential well
v0=50

#set constants
h = 197*1e-9
m = 0.511*1e6
# E = 413
a=1.e-11

# Define position space
x = np.linspace(-10*a,10*a,100)

def bisect(f, a, b, max_Iter, tolerance):
    
    
    if f(a)*f(b) > 0: # If a and b don't bracket, then stop now
        print("Error:", a, " and ", b, " do not bracket the solution")
        return "null"
    
    for i in range(max_Iter):
        guess=(a+b)/2
        
        if abs(f(guess))<10**(tolerance): # If we are "close enough" return this value
            return guess
        
        if f(a)*f(guess) > 0:
            a = guess
        else:
            b = guess
            
    return guess

# define function that retunrs the wavefunctiona at the boundary
def schro_boundary(E):
    sol = odeint(schro, V0, x, args=(E,), tfirst = True)
    dpsi = sol[:,0]
    ddpsi = sol[:,1]
    
    plt.plot(x,dpsi)
    plt.plot(x[25:-25],dpsi[25:-25])
    return dpsi[-1]

#define schodinger system of differential equations
def schro(x,V,E):
    psi = V[0]
    dpsi = V[1]
    ddpsi = 2*m/(h**2)*(v0*((x**2)/(a**2))-E)*psi
    
    #pack results
    rate = np.array([dpsi, ddpsi])
    return rate

#find ground state energy
Gnd_energy = bisect(schro_boundary,100,200,100,-3)
    
print("The proper eigenvalue for the ground state of this harmonic oscilattor")
print("is: ",Gnd_energy, "eV")

E = Gnd_energy
sol = odeint(schro, V0, x, args=(E,), tfirst=True)
p = sol[:,0]
dp = sol[:,1]

#graph ground state
fig2, (ax2) = plt.subplots(nrows=1, ncols=1)
ax2.plot(x[25:-25],p[25:-25], label='E=137.8')
