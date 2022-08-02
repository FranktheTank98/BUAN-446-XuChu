#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 17:03:25 2022

@author: xuchu
"""

# Exercise 7.9

import numpy as np

numbers = np.arange(1, 16).reshape(3, 5)

numbers

# Part a
numbers[2]

# **INSTRUCTOR NOTE: Part b should say "Select column 4"
# Part b
numbers[:, 4]

# Part c
numbers[:, 0:2]

# Part d
numbers[:, 2:5]

# Part e
numbers[1, 4]

# Part f
numbers[1:3, [0, 2, 4]]