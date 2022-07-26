#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 23:13:18 2022

@author: xuchu
"""

# Exercise 6.5

"""Tokenizing a string and counting duplicate words."""

text = ('this is sample text with several words ' 
        'this is more sample text with some different words')

word_counts = {}

# count occurrences of each unique word
for word in text.split():
    if word in word_counts: 
        word_counts[word] += 1  # update existing key-value pair
    else:
        word_counts[word] = 1  # insert new key-value pair

print(f'{"WORD":<12}COUNT')

for word, count in sorted(word_counts.items()):
    if count > 1:
        print(f'{word:<12}{count}')