# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 14:44:22 2014

@author: ychen1 (Cynthia (Yun-Hsin) Chen)
"""
x = int(raw_input('What is your value for x?\n'))
y = int(raw_input('What is your value for y?\n'))

def comparefunction(x,y):
    if x > y:
        return 1
    elif x ==y:
        return 0
    elif x < y:
        return -1
        
print comparefunction(x,y)