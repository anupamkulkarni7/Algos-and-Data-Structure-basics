#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 19:06:28 2019

@author: illuminatus
"""

from data_structures import stack_queue

a1 = myStack()
a1.push(3); a1.push(7); a1.push(5); a1.push(11); a1.push(1)
print(a1.size())

a1s = StackSort(a1)
while a1s.size() != 0:
    print(a1s.pop())


a2 = stack_queue.SetOfStacks(3)
a2.push(3); a2.push(4); a2.push(5)




#   --------------------------------------------------------------------------

def StackSort(s1):
    
    s2 = myStack()
    s2.push(s1.pop())
    
    while s1.size() != 0:
        temp = s1.pop()
        while temp < s2.top() and s2.size() != 0:
            s1.push(s2.pop())
        
        s2.push(temp)
    
    return s2