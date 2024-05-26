#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 14:12:30 2024

@author: sebastian
"""

import numpy as np

a = np.eye(5, dtype="int")
a[3:, :2] = 2
a[:2, 3:] = 3
print(a)
print("\n")
b = np.identity(5, dtype="int")
b[3:, :2] = 2
b[:2, 3:] = 3
print(b)
