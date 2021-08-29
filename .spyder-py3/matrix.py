# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 14:48:17 2021

@author: Kedar
"""

"""
Matrices
"""
import numpy.linalg as la
from scipy.integrate import odeint
from scipy.optimize import brentq
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot,xlabel,ylabel,legend,show, figure, subplot

# define matrix
M=np.array([[1,2,3],[2,3,1],[4,3,1]])
# M=np.eye(3)
w,v = la.eig(M)

print('First:',w[0], v[:,0])
print('Second:',w[1], v[:,1])
print("third:", w[2], v[:,2])

print("\n")
print("running over all eigenvalues we have")
for i in range(np.shape(M)[0]):
    # choose lambda and eigenvector
    L = w[i]
    X = v[:,i]
    #print Ax
    print("Ax=",np.matmul(M,X))
    print("Lx=",L*X)
    
    # print  (A-LI)*X
    print("(A-L*I)*X=",np.round(np.matmul(M-L*np.eye(np.shape(M)[0]),X),3))
    print(" ")

print(np.ones(2,float,2))