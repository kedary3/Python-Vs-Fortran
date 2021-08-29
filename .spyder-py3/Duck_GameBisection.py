# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 14:47:32 2021

@author: Kedar
"""
import sys
from scipy.optimize import newton, brentq
import numpy as np

def quad(x):
    y = (x-20)*(x+1)
    return y

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


print(' [0, 100] ',bisect(quad,0,100,1000,-5))
print(' [0, 100] ',newton(quad, 50))
print(' [0, 100] ',brentq(quad, 0,100))
print(' [0, -100] ',bisect(quad,-100,0,1000,-5))
print(' [0, -100] ',newton(quad, -50))
print(' [0, -100] ',brentq(quad, 0,-100))

duck_density=0.3

def duckfloat(d):
    
    if(d>2*radius):
        
        print("duck is not floating, it is fully submerged")
        return 1
    
    duck_Mass= duck_density*(4/3)*np.pi*radius**3
    submerged_Vol=(np.pi/3)*(3*radius*d**2 - d**3)
    
    water_density = 1
    # water_mass = 1*submerged_Vol
    
    #duck_mass-water_mass = duck_density*duck_Vol - water_density*submerged_Vol 
    return duck_Mass - water_density*submerged_Vol 

for radius in range(1,10):
    
    print("duck game number:", radius)
    print("the duck density is, ", duck_density, "g/cm^3 and the radius is ", radius, " cm")
    print("[", 0, ",", radius,"]:" ,'For the Bisect method the root is:',       bisect(duckfloat,0,radius,1000,-100))
    print("[", 0, ",", radius,"]:" ,'For the Newton method the root is:',       newton(duckfloat, radius))
    print("[", 0, ",", radius,"]:" ,'For the Brentq method the root is:',       brentq(duckfloat, 0,radius))



#it appears that the duck can barely submerge 
    
"""
At what depth does a duck float in water? We can model a duck as a sphere with radius 10 cm. Trust me, I found it on the internets:

A Spherical Duck

The duck will float when the weight of the water it displaces equals the weight of the duck. 

Write an equation for the volume of water displaced when the duck sinks a depth d. What is the mass of this water? What is the mass of the duck? When these are equal, the duck floats, which gives our basic equation. 
Rearrange the equation so the right-hand side is the difference in masses. Our goal is to find values of d that are roots of this equation (ie that make this difference zero), when the duck floats. 
Define a python function that evaluates this difference as a function of d.
def duckfloat(d):
     ....
Do we know the range of possible values for d [a, b]? Or do we have a good guess of what d might be (d0)?

Use either brentq or newton to find a root near d0 or in the range [a, b].
Check to make sure the result makes sense. In particular, check that d < 2r, because otherwise the volume equation doesn’t work!
Try different values of ρ and r and see if you get the effect you expect. What happens as ρ increases?  Goes to zero? What happens as r increases? Goes to zero?
Use the following formulas and constants:

The volume of a sphere with radius r is V = (4/3) π r3.

Assume the density of a duck, ρ, is 0.3g/cm3  (about 1/3 the density of water). (What is it's total mass ?)

If a sphere with radius r is submerged in water to a depth d, the volume of the sphere below the water line is

volume = (π/3)  ( 3 r d2 − d3 ) as long as d < 2r 

An object floats at the level where the weight of the displaced water equals the total weight of the object, or equivalently, where their mass are equal.
"""