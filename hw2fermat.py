# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 13:48:01 2014

@author: ychen1 (Cynthia (Yun-Hsin) Chen)
"""

a = int(raw_input('What is your value a?\n'))
b = int(raw_input('What is your value b?\n'))
c = int(raw_input('What is your value c?\n'))
n = int(raw_input('What is your value n?\n'))

def check_fermat(a,b,c,n):
    if n>2 and (a**n)+(b**n)==(c**n):
        print"Holy smokes, Fermat was wrong!"
    else: 
        print "No, that doesn't work."


"""
check_fermat(a,b,c,n)        
"""