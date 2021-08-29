# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 2020

@author: Kedar
"""

import numpy as np
chi=0
O=[7,30,72,57,26,8]
E=[4,27,68,68,27,4]
for i in range(np.shape(E)[0]):
    chi += ((O[i]-E[i])**2)/E[i]
print(chi)  