#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Exercise 4.9
def fahrenheit(celsius):
    return (9 / 5) * celsius + 32

print('Celcius', '\t','Fahrenheit')

for celsius in range(101):
    print(f'{celsius:10}{fahrenheit(celsius):10.1f}')


# In[ ]:




