#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 14:40:28 2024

@author: sebastian
"""

import numpy as np

d = np.arange(1, 11)
D = np.tile(d, (10, 1))
print(D)
 
print(D.sum(axis = 0))