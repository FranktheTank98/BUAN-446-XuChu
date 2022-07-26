#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 22:58:44 2022

@author: xuchu
"""

#Assignment 3 - Execrise 5.15

#a
invoices = [(83, 'Electric sander', 7, 57.98), 
            (24, 'Power saw', 18, 99.99),
            (7, 'Sledge hammer', 11, 21.50),
            (77, 'Hammer', 76, 11.99),
            (39, 'Jig saw', 3, 79.50)]

from operator import itemgetter

for part, description, quantity, price in sorted(invoices, key=itemgetter(1)):
    print(f'{part:>2}  {description:<16}{quantity:>3}{price:>7.2f}')
    

#b
for part, description, quantity, price in sorted(invoices, key=itemgetter(3)):
    print(f'{part:>2}  {description:<16}{quantity:>3}{price:>7.2f}')


#c
quantity = [(description, quantity) for part, description, quantity, price in invoices]

for description, quantity in sorted(quantity, key=itemgetter(1)):
    print(f'{description:<16}  {quantity:>2}')
    

#d
value = [(quantity * price, description) for part, description, quantity, price in invoices]
    
for  value, description in sorted(value, key=itemgetter(0)):
    print(f'{description:<16}  {value:>8.2f}')
    
    
#e
value2 = [(quantity * price, description) for part, description, quantity, price in invoices if 200 <= price * quantity <=500]

for  value, description in sorted(value2, key=itemgetter(0)):
    print(f'{description:<16}  {value:>8.2f}')
    
    
#f
total = sum([quantity * price for part, description, quantity, price in invoices])
print(f'Total amount is {total}')