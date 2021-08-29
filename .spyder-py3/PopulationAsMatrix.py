# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 20:17:35 2021

@author: Kedar
"""
"""
On a monthly basis (see chart below):

400 people move into the Seattle area by means of the Downtown area.

10% of the Downtown population moves to Capitol Hill and 10% moves to Ballard.

10% of the Capitol Hill population moves back to Downtown, 20% moves to Ballard, and 10% moves to the U-district.

20% of the Ballard population also moves to the U-district, while 30% moves to Fremont.

From the U-district, 10% moves to Capitol Hill and 10% moves to Ballard.

100 people move out of the Seattle area from each of Capitol Hill and Ballard. 20% of the U-district population and 50% of the Fremont population also leaves the Seattle area.

Denote LaTeX: x_1,\:x_2,\:x_3,\:x_4,\:and\:x_5x 1 , x 2 , x 3 , x 4 , a n d x 5 as the population of the Downtown area, Capital Hill, Ballard, the U-district, and Fremont, respectively.

If the change in population of each neighborhood  from one month to the next is LaTeX: y_1,\:y_2,\:y_3,\:y_4,\:and\:y_5y 1 , y 2 , y 3 , y 4 , a n d y 5, then we can write the equation for the change in population for Downtown as

LaTeX: -0.2x_1+0.1x_2+0x_3+0x_4+0x_5+400=y_1− 0.2 x 1 + 0.1 x 2 + 0 x 3 + 0 x 4 + 0 x 5 + 400 = y 1

And so forth for each neighborhood giving a system of five equations. In matrix form, the full system is: LaTeX: A\vec{x} + \vec{b}=\vec{y}A x → + b → = y →.  By hand, write out the full system and the matrix A and b.

Assignment:

Write code in python to:

1) Fill in the matrix A and vector b

2) Start with a population of 400 people in each neighborhood ( x = [400 400 400 400 400 ]) and apply the matrix relationship to find

a) change in population for one month, y

b) update the population after first month by adding the change to the initial value

3) Loop to find population after 12 months.

hw2_fig.png 

 

Matrices in Python: 

Form a matrix using the array function in numpy. Specify elements by listing each row within [...], and the whole matrix in outer [...]. Matrix multiplication is done with the @ operator. Note that Python treats a 1-d array as a column vector for multiplication. Matrix addition is just normal addition.

"""
import numpy as np
from numpy import shape, array
import matplotlib.pyplot as plt

#initial conditions
X = [[400],[400],[400],[400],[400]]
"""
describe the relationships as a set of equations
y1 = 400 - 0.2x1 +0.1x2 +0(x3+x4+x5)
y2 = -100 + 0.1x1-0.4x2+0x3+0.1x4 +0x5
y3 = -100 +0.1x1+0.2x2-0.5x3+0.1x4 +0x5
y4 = 0 + 0x1 +0.1x2 +0.2x3 -0.4x4 + 0x5
y5 = 0 +0x1 +0x2+ 0.3x3 +0x4 -0.5x5
y = b + Ax
"""
#initialize vectors
b = [[400],[-100],[-100],[0],[0]]
A = [[-0.2,0.1,0,0,0],[0.1,-0.4,0,0.1,0],[0.1,0.2,-0.5,0.1,0],[0,0.1,0.2,-0.4,0],[0,0,0.3,0,-0.5]]

locations = ["Downtown", "Capital Hill", "Ballard", "U-district", "Fremont"]
months =24 #more months for animation
for i in range(months):
    y=np.matmul(A,X)+b #@ wasnt working for me. I think this is a typo in the instructions right?
    X=X+y
    if (i==0): #describe change after one month
        for location in locations:
            print("In the first month, the change for "+location + " is:" , y[locations.index(location)][0])
    
    #plot total population and change in population per month per location
    fig, ax = plt.subplots(2)
    fig.suptitle("Population and Change In Population")
    ax[0].bar(locations,X.flatten())
    ax[1].bar(locations,y.flatten())
    plt.show()    

 