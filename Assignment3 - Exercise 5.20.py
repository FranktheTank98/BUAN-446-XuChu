#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 23:00:15 2022

@author: xuchu
"""

#Assignment 3 - Execrise 5.20

def display_table(a, width):
    """receive 2 dimensions and tranfer it to a table"""
    
    
    print(f'{"":{width}}', end='')
    
    for row_index, row in enumerate(a):
        column = list(column_index for column_index, value in enumerate(row) if row_index == 0)
  
        for index in column:
            print(f'{index:> {width}}', end = '')
        
        print()
        print(f'{row_index:> {width}}', end= '')
        
        
        for column_index, value in enumerate(row): 
            print(f'{value:> {width}}', end = '')
       
        
            
            
values = [list(range(90, 100)), 
          list(range(100, 110)), 
          list(range(110, 120)), 
          list(range(120, 130)), 
          list(range(130, 140)), 
          list(range(140, 150)), 
          list(range(150, 160)), 
          list(range(160, 170)), 
          list(range(170, 180)), 
          list(range(180, 190)), 
          list(range(190, 200))]

display_table(values, 5)