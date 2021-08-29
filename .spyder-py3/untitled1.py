# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 19:54:49 2020

@author: Kedar
"""
import numpy as np
t=[0.7, 0.3, 0.9, 0.3, 0.6, 0.9, 0.8, 0.7, 0.8, 1.2, 0.5, 0.9, 0.9, 0.3]
print(np.std(t,ddof=1))
print(np.mean(t))