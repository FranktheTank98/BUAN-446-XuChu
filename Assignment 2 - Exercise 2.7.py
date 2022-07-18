#!/usr/bin/env python
# coding: utf-8

# In[19]:


# Exercise 2.8

print('number   square  cube')
print(0, '\t', 0 ** 2, '\t', 0 ** 3)
print(1, '\t', 1 ** 2, '\t', 1 ** 3)
print(2, '\t', 2 ** 2, '\t', 2 ** 3)
print(3, '\t', 3 ** 2, '\t', 3 ** 3)
print(4, '\t', 4 ** 2, '\t', 4 ** 3)
print(5, '\t', 5 ** 2, '\t', 5 ** 3)


# In[5]:


# Exercise 2.12

print('Amount after 10 years:', 1000 * (1 + .07) ** 10)

print('Amount after 20 years:', 1000 * (1 + .07) ** 20)

print('Amount after 30 years:', 1000 * (1 + .07) ** 30)


# In[25]:


# Exercise 3.1
"""Using nested control statements to analyze examination results."""

passes = 0 

for student in range(10):
    result = int(input('Enter result (1=pass, 2=fail): '))
    
    while result != 1 and result != 2:  
        print('Incorrect result entered.')
        result = int(input('Enter result (1=pass, 2=fail): '))
        
    if result == 1:
        passes = passes + 1

print('Passed:', passes)
print('Failed:', 10 - passes)

if passes > 8:
    print('Bonus to instructor')


# In[23]:


# Exercise 3.6
input('What is your problem? ')

response = input('Have you had this problem before (yes or no)? ')

if response == 'yes':
    print('Well, you have it again.')
else:
    print('Well, you have it now.')


# In[22]:


# Exercise 3.6
input('What is your problem? ')

response = input('Have you had this problem before (yes or no)? ')

if response == 'yes':
    print('Well, you have it again.')
else:
    print('Well, you have it now.')


# In[24]:


# This conversation won't be able to convince the people since there are only two repeating answers.


# In[26]:


# Exercise 3.10
principal = 1000.0
rate = 0.07

for year in range(1, 31):
    print(f'Amount after {year} year(s): {principal * (1 + rate) ** year:.2f}')


# In[27]:


# Exercise 3.16
"""Find the two largest integers."""

largest = int(input('Enter number: '))
number = int(input('Enter number: '))

if number > largest:
    next_largest = largest
    largest = number
else:
    next_largest = number

for counter in range(2, 10):
    number = int(input('Enter number: '))

    if number > largest:
        next_largest = largest
        largest = number
    elif number > next_largest:
        next_largest = number

print(f'Largest is {largest}\nSecond largest is {next_largest}')


# In[28]:


# Exercise 4.9
def fahrenheit(celsius):
    return (9 / 5) * celsius + 32

print('Celcius', '\t','Fahrenheit')

for celsius in range(101):
    print(f'{celsius:10}{fahrenheit(celsius):10.1f}')


# In[29]:


# Exercise 4.12
"""The race between the tortoise and the hare."""
import random

RACE_END = 70  

def move_tortoise(tortoise):
    """Move tortoise's position."""
    move = random.randrange(1, 11)  # randomize move to choose

    # determine moves by percent
    if 1 <= move <= 5:  # fast plod
        tortoise += 3
    elif move in (6, 7):  # slip
        tortoise -= 6
    else:  # slow plod
        tortoise += 1

    # ensure tortoise doesn't slip beyond start position or past the finish
    if tortoise < 1:
        tortoise = 1
    elif tortoise > RACE_END: 
        tortoise = RACE_END

    return tortoise

def move_hare(hare):
    """Move hare's position."""
    move = random.randrange(1, 11)  # randomize move to choose
      
    # determine moves by percent
    if move in (3, 4):  # big hop
        hare += 9
    elif move == 5:  # big slip
        hare -= 12
    elif 6 <= move <= 8:  # small hop
        hare += 1
    elif move > 8:  # small slip
        hare -= 2

    # ensure hare doesn't slip beyond start position or past the finish
    if hare < 1:
        hare = 1
    elif hare > RACE_END: 
        hare = RACE_END

    return hare

def print_positions(tortoise, hare):
    """Display positions of tortoise and hare.

    Goes through all 70 squares, printing H if hare 
    on position and T for tortoise"""

    for count in range(1, RACE_END + 1):
        # tortoise and hare positions collide
        if count == tortoise and count == hare:
            print('OUCH!!!', end='')
        elif count == hare:
            print('H', end='')
        elif count == tortoise:
            print('T', end='')
        else:
            print(' ', end='')
        
    print()

tortoise = 1
hare = 1
timer = 0

print('ON YOUR MARK, GET SET')
print('BANG !!!!!')
print("AND THEY'RE OFF !!!!!")

while tortoise < RACE_END and hare < RACE_END: 
    hare = move_hare(hare)
    tortoise = move_tortoise(tortoise)
    print_positions(tortoise, hare)
    timer += 1

# tortoise beats hare or a tie
if tortoise >= hare:
    print('\nTORTOISE WINS!!! YAY!!!')
else:  # hare beat tortoise
    print('\nHare wins. Yuch!')

print(f'TIME ELAPSED = {timer} seconds')


# In[ ]:




