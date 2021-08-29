# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 12:34:08 2021

@author: Kedar
"""
import numpy as np
import matplotlib.pyplot as plt
# Stick Game
# 1) 100 children stand in a line. The first one holds a basket full of sticks. Initially, none of the children has a stick.

# 2) Each child along the line takes a turn as "runner" and carries the basket of sticks. The runner starts with themselves and walks down the line of children giving or taking away sticks. After they are done, the runners return to their position, handing the basket off to the next runner, and are done for the game.

# 3) The runner goes down the line of children, starting with themselves. 
#  For each child whose position is a multiple of their own, then 
#  * if the child has a stick, the runner takes it away.
#  * if the child has no stick, the runner gives a stick.
# (ie if runner is in position 7, they check whether they and child 17 21 28 etc have sticks)

# Who has a stick at the end of the game?

# Hint:

# Create an array sticks = zeros(100) containing the number of sticks each child holds. The values in sticks can only be either 0 or 1 according to the rules.

# Be careful with array indexing: child #1 is indicated by sticks[0]

# You have two options for modeling the runner:
# a) Use the % operator to find modulus (remainder on division) to check if each child is a multiple
# b) Use a step size in the range function to skip over children as the runner goes down the line

# Rental Cars
# A car rental company has two locations, Albany and Boston. Some customers do “one-way rentals,” picking up a car in Albany and returning it in Boston, or the other way around. Each week 5% of the cars in Albany are dropped off in Boston, and 3% of the cars in Boston get dropped off in Albany. At the beginning of the year, there are 150 cars at each location.

# Write a program that plots the number of cars in Albany and Boston each week for 1 year (52 weeks) to find if the number of cars eventually stays the same. Mark both cities on the same plot with different symbols or colors.

# Hints:

# Create arrays boston and albany to contain the 52 values using the zeros function.

# First write the lines of code that update the number of cars in each location from one week to the next. Initialize the variables Albany and Boston with the number of cars in each location at the beginning of the week. Calculate the number of cars moving Albany->Boston and Boston->Albany. Then compute the next values for the arrays albany and boston.

# Put this in a loop to repeat for 52 weeks

# Add commands to plot a the number of cars at each week using the pyplot package https://matplotlib.org/tutorials/introductory/pyplot.html

# Note: cars are countable things, so a and b should always be integer values. You can use the rint (Links to an external site.) function to round off the number of cars that move during each week. (Type "help round")

# You can start your program like this:

# from numpy import zeros, rint
# from pyplot import plot, xlabel, ylabel, show

# nweek=52 
# albany = zeros(nweek)
# boston = zeros(nweek)
def stick_Game():
    kids = np.zeros(100)
    for k in range(100):
        for i in range(k,100,k+1):
            if(kids[i]==0):
                    kids[i]=1
            else:
                    kids[i]=0   
    squares=[]
    for i in range(np.size(kids)):
        if kids[i]==1:
            squares.append(i+1)
    print("the positions that have stcks are:" , squares)
def car_Rental():
    albany_Array=np.zeros(52)
    boston_Array=np.zeros(52)
    albany_Cars=150
    boston_Cars=150
    boston_to_albany_Factor=0.03
    albany_to_boston_Factor=0.05
    albany_Array[0]=150
    boston_Array[0]=150
    for i in range(1,52):
        current_albany_Cars=albany_Cars
        current_boston_Cars=boston_Cars   
        albany_Cars=current_albany_Cars + np.rint(boston_to_albany_Factor*current_boston_Cars)
        albany_Cars = albany_Cars - np.rint(albany_to_boston_Factor*current_albany_Cars)
        
        boston_Cars=current_boston_Cars + np.rint(albany_to_boston_Factor*current_albany_Cars)
        boston_Cars= boston_Cars - np.rint(boston_to_albany_Factor*current_boston_Cars)
       
        boston_Array[i]=boston_Cars
        albany_Array[i]=albany_Cars
    print("over the course of a year, Albany has this many cars:" , albany_Array)
    print("over the course of a year, Boston has this many cars:" , boston_Array)
    time=np.arange(52)
    plt.plot(time,albany_Array, label="Albany Car Volume")
    plt.plot(time,boston_Array, label="Boston Car Volume")
    plt.xlabel("Time (weeks)")
    plt.ylabel("Car Volume")
    plt.title("Rental Car volume in Albany and Boston Over Time")
    plt.legend(loc="upper left")
    plt.show()
car_Rental()  
stick_Game()    
# important to remember that if you do a scatter plot on an initialized figure and use oop to 
# update the figure in the loop, we dont have to use so much memory storing the entire array and appending it