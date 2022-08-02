#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 17:03:51 2022

@author: xuchu
"""

# Exercise 7.14

import numpy as np

array1 = np.array([[0, 1], [2, 3]])

array1

array2 = np.array([[4, 5], [6, 7]])

array2

array3 = np.vstack((array1, array2))

array3

array4 = np.hstack((array1, array2))

array4

array5 = np.vstack((array4, array4))

array5

array6 = np.hstack((array3, array3))

array6