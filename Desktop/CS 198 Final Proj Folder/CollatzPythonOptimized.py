# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 04:00:00 2021

@author: Kedar
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 22:07:21 2021

@author: Kedar
"""

import numpy as np
import sys
import matplotlib.pyplot as plt



MAX = 100000000000000
cycleStyle = True



def steps(x,m,a):  #method to iterate over an input integer domain, i.e.Collatz[-100,100]
    stepList = [0]*(2*x+1)
    n = -1*x
    while(n<=x):
        stepList[n+x] = getSteps(n,cycleStyle,m,a)  
        n+=1
    return stepList
def getSteps(x,cycleStyle,m,a): #determines the number of iterations towards 1 or the number of steps in a cycle
    steps = 0
    cycleList =[]
    cycleList.append(x)
    while(x!=1):
        if(x>MAX):
            print("Abort")
            sys.exit(1)
        elif(x%2==1):
            x = (m*x +a)/2
            steps+=2
            cycleList.append(x)
        else:
            x = x/2
            steps+=1
            cycleList.append(x)
        if(cycleStyle):
            if(isCycle(cycleList)):
                return len(cycleList)*-1
    return steps
    
def isCycle(cycleList): #method to determine if a trajectory contains a cycle
    if(len(cycleList)==1):
        return False
    else:
        t = cycleList[-1]
        cycleList.remove(cycleList[-1])
        if t in cycleList:
            cycleList.append(t)
            return True
        else:
            cycleList.append(t)
            return False
def Collatz_main(n,m,a): #method to get step values and write them to file 
   
    
    d = list(map(int, steps(n,m,a)))
    
    
    # ar = np.arange(-n,n+1,1)
    
    # with open(file="Python_Collatz_n= "+str(n)+" m= "+str(m)+" a= "+str(a)+".dat",mode="w") as f:
    #     for index in range(len(d)):
    #         f.writelines(str(d[index])+"\n")
            
    #     f.close()
    # plt.scatter(ar,d, marker=".",linewidth=0)
    # plt.title("Steps to Reach 1 Versus Starting Number")
    # plt.ylabel("Steps")
    # plt.xlabel("Starting Number")
    # plt.xlim(0,n)
    # plt.ylim(0,500)
    # plt.show()
    

def main():
    import time
    
    for exponent in range(1, 7):
        time_start = time.time()
        Collatz_main(10**exponent,3,1)
        print("N=",10**exponent,": ",time.time()-time_start,)

main()

