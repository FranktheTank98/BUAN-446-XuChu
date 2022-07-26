#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 22:51:53 2022

@author: xuchu
"""

# Exercise 5.11

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def summarize_letters(string):
    letters = []
    counts = []
    
    for letter in string.lower():
        if letter in ALPHABET:
            if letter in letters:
                index = letters.index(letter)
                counts[index] += 1
            else:
                letters.append(letter)
                counts.append(1)
           
    tuples = list(zip(letters, counts))
    tuples.sort()
    return tuples

panagram = 'The Quick Brown Fox Jumps Over The Lazy Dog'
summary = summarize_letters(panagram)


for char, count in summary:
    print(f'{char}: {count}')


all_letters = True

if len(summary) == len(ALPHABET):
    for item in summary:
        if item[0] not in ALPHABET:
            all_letters = False
            break  
else:
    all_letters = False

if all_letters:
    print(f'"{panagram}" contains all the letters in the alphabet')
else:
    print(f'"{panagram}" does not contain all the letters in the alphabet')