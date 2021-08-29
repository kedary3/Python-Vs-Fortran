# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 17:33:46 2021

@author: Kedar
"""
"""
# BPHYS 450 HW 1: Quantum tunneling and Lorenz
# Kedar Yadav
# January 11, 2020
"""

# Exercise 1: Quantum Potential Step

# A basic quantum mechanics problem involves a particle of mass m that encounters a one-dimensional potential step, like this:

# Step

# The particle with initial kinetic energy E and wavevector LaTeX: k_1 = \frac{\sqrt{2mE}}{\bar{h}}k 1 = 2 m E h ¯ enters from the left and encounters a sudden jump in potential energy of height V at position x = 0. By solving the Schrodinger equation, one can show that when E > V the particle may either (a) pass the step, in which case it has a lower kinetic energy of E − V on the other side and a correspondingly smaller wavevector of LaTeX: k_2 = \frac{\sqrt{2m(E-V)}}{\bar{h}}k 2 = 2 m ( E − V ) h ¯ , or (b) it may be reflected, keeping all of its kinetic energy and an unchanged wavevector but moving in the opposite direction. The probabilities T and R for transmission and reflection are given by

# T & R Eqn
# Suppose we have a particle with mass equal to the electron mass m = 9.11×10−31 kg and energy 10 eV encountering a potential step of height 9 eV. Write a python program to compute and print out the transmission and reflection probabilities using the formulas above. Make your output be informative, and structure and comment your program so it is easy to read -- in particular, do not use numerical values in your formulas, but define them on separate lines.
 
# Exercise 2: Lorenz
# A certain famous system of differential equations can be approximated by a system of difference equations that looks like this:

# LaTeX: x_{i+1} = x_i + σ (y_i − x_i) dt \\

# y_{i+1} = y_i + [x_i(r − z_i) − y_i] dt \\

# z_{i+1} = z_i + (x_iy_i − bz_i) dt 
# x i + 1 = x i + σ ( y i − x i ) d t y i + 1 = y i + [ x i ( r − z i ) − y i ] d t z i + 1 = z i + ( x i y i − b z i ) d t

# • Write a program that computes the first 1000 elements of the sequences LaTeX: x_i, y_i, z_ix i , y i , z i  and stores them in vectors named x, y, and z.

# • Use the initial values x[0] = 1, y[0] = 2 and z[0] = 3, with values σ = 10, b = 8/3 and r = 28, and with time step dt = 0.01. 
import numpy as np
import scipy.constants as sc
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.animation import FuncAnimation, PillowWriter 

def Quantum_Potential_Step( mass, energy, barrier_potential ):
    
    #Define initial state
    initial_Wavevector = np.sqrt(2*mass*energy)/sc.hbar
    
    #Define final state
    final_Wavevector = np.sqrt(2*mass*(energy-barrier_potential))/sc.hbar
    
    #Calculate probabilities
    Transmission_Probability = 4*initial_Wavevector*final_Wavevector/((initial_Wavevector+final_Wavevector)**2)
    Reflection_Probability = ((initial_Wavevector-final_Wavevector)/(initial_Wavevector+final_Wavevector))**2
    #Report
    print("given a mass of ", mass,  "kg and an initial energy of ", energy, "eV and a potential barrier of ", barrier_potential, "eV:" )
    print("the transmission probability is {:0.2f}\n".format(Transmission_Probability), "\nand the reflection probability is {:0.2f}\n".format(Reflection_Probability))

def Lorenz(rho,b,r,init_x,init_y,init_z,timestep,iterations):
    #define vector
    x=[init_x]
    y=[init_y]
    z=[init_z]
    
    #perform iterations
    
    for i in range(1,iterations-1):
        
        x.append(x[i-1]+rho*(y[i-1]-x[i-1])*timestep)
        
        y.append(y[i-1]+(x[i-1]*(r-z[i-1])-y[i-1])*timestep)
        
        z.append(z[i-1]+(x[i-1]*y[i-1]-b*z[i-1])*timestep)
    
    #Graph
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot(x, y, z)
    plt.show()
    
def Lorenz_Animation(rho,b,r,init_x,init_y,init_z,timestep,iterations):
    
    #define vector start
    x=[init_x]
    y=[init_y]
    z=[init_z]
    
    
    #Define plot
    fig = plt.figure()
    ax = fig.gca(projection='3d')
   
    
    line, = ax.plot(x, y, z, '-')
             
   
    #set graph zoom           
    ax.set_xlim((-25, 25))
    ax.set_ylim((-35, 35))
    ax.set_zlim((5, 55))
    
    #set inital state on which to draw 
    def init():
        
        line.set_data([], [])
        line.set_3d_properties([])

        
        return line,
    #perform iterations  
    def animate(i):
        x.append(x[i-1]+rho*(y[i-1]-x[i-1])*timestep)
        
        y.append(y[i-1]+(x[i-1]*(r-z[i-1])-y[i-1])*timestep)
        
        z.append(z[i-1]+(x[i-1]*y[i-1]-b*z[i-1])*timestep)
        line.set_data(x,y)
        line.set_3d_properties(z)
        return line,
    
    #call animation
    anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=iterations, interval=200, blit=True)
    #define writer
    writer = PillowWriter(fps=25)  
    
    #saev as gif
    anim.save("Lorenz.gif", writer=writer)  
    #Graph
    plt.show()
#Execute
Quantum_Potential_Step(9.11*10**-31, 10, 9)
Lorenz(10,8/3,28,1,2,3,0.01,2000)
Lorenz_Animation(10,8/3,28,1,2,3,0.01,1000)