#!/usr/bin/env python
# coding: utf-8

# In[234]:


import random
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
draw1 = random.randrange(0,13)
draw2 = random.randrange(0,13)
card1 = deck[draw1]
card2 = deck[draw2]
print(card1)
print(card2)


# In[235]:


if card1 == 'J' or card1 == 'Q' or card1 == 'K':
    score1 = 10
    name1 = card1
elif card1 == 'A':
    score1 = 11
    name1 = card1
else:
    score1 = deck[draw1]
if card2 == 'J' or card2 == 'Q' or card2 == 'K':
    score2 = 10
    name2 = card2
elif card2 == 'A':
    score2 = 11
    name2 = card2
else:
    score2 = deck[draw2]
print(f'Player drawed {card1} + {card2}')
total_score = score1 + score2
print(f'Player drawed {score1} + {score2} = {total_score}')


# In[ ]:




