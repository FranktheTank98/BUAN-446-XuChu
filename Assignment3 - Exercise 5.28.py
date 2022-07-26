#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 23:09:05 2022

@author: xuchu
"""

#Assginment 3 - Execrise 5.28



import numpy as np
import statistics as stats

responses = [1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 5]
values, counts = np.unique(responses, return_counts=True)
values = list(values)
counts = list(counts)

print('Reponses and frequencies:')
for value, count in zip(values, counts):
    print(f'{value}: {count}')

print(f'Min response count: {values[counts.index(min(counts))]} occurred {min(counts)} time(s)')
print(f'Max response count: {values[counts.index(max(counts))]} occurred {max(counts)} time(s)')
print(f'Range of response counts: {min(counts)}-{max(counts)}')
print(f'Mean response count: {stats.mean(counts)}')
print(f'Median response count: {stats.median(counts)}')
print(f'Mode response count: {stats.mode(counts)}')
print(f'Variance: {stats.pvariance(counts)}')
print(f'Standard deviation: {stats.pstdev(counts)}')
