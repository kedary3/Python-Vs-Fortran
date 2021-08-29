# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 20:57:58 2021

@author: Kedar
"""

from mpl_toolkits import mplot3d

import numpy as np
import matplotlib.pyplot as plt




# # Data for a three-dimensional line
# zline = np.linspace(0, 15, 1000)
# xline = np.sin(zline)
# yline = np.cos(zline)
# ax.plot3D(xline, yline, zline, 'gray')

# Data for three-dimensional scattered points
def phi0(x):
    return (1/(np.pi**(1/4)))*np.e**(-1*(x**2)/2)
def phi1(y):
    return (np.sqrt(2)/(np.pi**(1/4)))*y*np.e**(-1*(y**2)/2)
def p(x,y):
    return np.abs(phi0(x)*phi1(y))**2
xdata = np.linspace(-3,3,1000)
ydata = np.linspace(-3,3,1000)
X, Y = np.meshgrid(xdata, ydata)
Z = p(X,Y)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 60, cmap='viridis')
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('p(x1,x2)')
ax.view_init(60, 35)
fig.savefig("distinguishable particles")


def p_Boson(x,y):
    return 1/2*(np.abs(phi0(x))**2)*(np.abs(phi1(y))**2)+1/2*(phi0(x)*phi0(y))*(phi1(y)*phi1(x))+1/2*(phi0(y)*phi1(x)*phi0(x)*phi1(y))+1/2*(np.abs(phi0(y))**2)*(np.abs(phi1(x))**2)

xdata = np.linspace(-3,3,1000)
ydata = np.linspace(-3,3,1000)
X, Y = np.meshgrid(xdata, ydata)
Z = p_Boson(X,Y)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 60, cmap='viridis')
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('p(x1,x2)')
ax.view_init(60, 35)
fig.savefig("spin 0 boson")

def p_fermi(x,y):
    return 1/2*((np.abs(phi0(x))**2)*(np.abs(phi1(y))**2)-(phi0(x)*phi1(y)*phi1(x)*phi0(y))-(phi1(x)*phi0(y)*phi0(x)*phi1(y))+(np.abs(phi1(x))**2)*(np.abs(phi0(y))**2))

x = np.linspace(-3, 3, 30)
y = np.linspace(-3, 3, 30)

X, Y = np.meshgrid(x, y)
Z = p_fermi(X, Y)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 60, cmap='viridis')
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('p(x1,x2)');
ax.view_init(60, 35)
fig.savefig("spin half fermions")