# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 23:35:26 2021

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

P=1*10**7
n=1
T=300
R=8.3145
a=.4233
b=3.73*10**-5
def ideal_func(V):
    return P*V-(n*R*T)
def Van_der_Waals_func(V):
    return ((P+a*((n/V)**2))*(V-n*b))-n*R*T

print("there is a root at ",brentq(ideal_func,-1,1))
print("there is a root at ",brentq(Van_der_Waals_func,1,-1))

# V must be greater than n*b or less than n*b, 
# other wise one term will be zero and it will not be a root. 