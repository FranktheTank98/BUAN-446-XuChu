#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 17:39:56 2022

@author: xuchu
"""


import numpy as np
import random

#1 elements

%timeit rolls_array = np.random.randint(1, 7, 1)

#10 elements

%timeit rolls_array = np.random.randint(1, 7, 10)
%timeit list_a = [random.randrange(1, 7) for i in range(10)]

#100 elements

%timeit rolls_array = np.random.randint(1, 7, 100)
%timeit list_a = [random.randrange(1, 7) for i in range(100)]

#1000 elements

%timeit rolls_array = np.random.randint(1, 7, 1000)
%timeit list_a = [random.randrange(1, 7) for i in range(1000)]

#10000 elements

%timeit rolls_array = np.random.randint(1, 7, 1_0_000)
%timeit list_a = [random.randrange(1, 7) for i in range(10000)]

#100000 elements

%timeit rolls_array = np.random.randint(1, 7, 1_00_000)
%timeit list_a = [random.randrange(1, 7) for i in range(100000)]

#1000000 elements

%timeit rolls_array = np.random.randint(1, 7, 1_000_000)
%timeit list_a = [random.randrange(1, 7) for i in range(1000000)]
