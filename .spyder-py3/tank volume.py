# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 23:11:09 2021

@author: Kedar
"""
import sys
from scipy.optimize import newton, brentq
import numpy as np

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


D=10
V=45
C=1/2
def func(h):
    return (D**3*C*np.pi/12*(3*(h/D)**2-2*(h/D)**3))-V
print("The root is at ", bisect(func, 0,10,100,-3))

#depth must be between 0 and when the derivative is zero again, which is 10.
#function is graphed here: https://www.desmos.com/calculator/zyapbp6x0o