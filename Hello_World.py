#!/usr/bin/env python
# coding: utf-8

# In[10]:


hw_string = 'HELLO WORLD!'
hw_list = []
hw_list = hw_string

for i, char in enumerate(hw_list):
    pad = (i+1)*5
    print(f'{char: >{pad}}')

