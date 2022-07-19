#!/usr/bin/env python
# coding: utf-8

# In[1]:


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




