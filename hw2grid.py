# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 13:06:02 2014

@author: ychen1 (Cynthia (Yun-Hsin) Chen)
"""

"""
What the code should produce:
print '+','-','-','-','-','+','-','-','-','-','+'  
print '|',' '*7,'|',' '*7,'|'
print '|',' '*7,'|',' '*7,'|'
print '|',' '*7,'|',' '*7,'|'
print '|',' '*7,'|',' '*7,'|'
print '+','-','-','-','-','+','-','-','-','-','+'  
print '|',' '*7,'|',' '*7,'|'
print '|',' '*7,'|',' '*7,'|'
print '|',' '*7,'|',' '*7,'|'
print '|',' '*7,'|',' '*7,'|'
print '+','-','-','-','-','+','-','-','-','-','+'  
"""

grid1 = '+ '+'- '*4+'+ '+'- '*4+'+ '

grid2 = '| '+' '*8+'| '+' '*8+'| '

def topmiddlebottom():
    print grid1
    
def inbetween():
    print grid2

def do_twice():
    inbetween()
    inbetween()
    
def do_four():
    do_twice()
    do_twice()
    
def wholething():
    topmiddlebottom()
    do_four()
    topmiddlebottom()
    do_four()
    topmiddlebottom()
    
wholething()