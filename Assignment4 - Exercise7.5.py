#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 17:02:13 2022

@author: xuchu
"""

# Exercise 7.5

import numpy as np

powers = np.array([2 ** i for i in range(6)]).reshape(2, 3)

powers

powers.flatten()

powers

powers.ravel()

powers