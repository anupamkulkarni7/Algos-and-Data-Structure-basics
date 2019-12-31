#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 20:29:17 2019

@author: illuminatus
"""

class myStack():
    
    def __init__(self):
        self.data = []
        
    def pop(self):
        if len(self.data) > 0:
            return self.data.pop()
        else:
            print("Stack empty.")
            return
    
    def push(self,val):
        return self.data.append(val)
    
    def top(self):
        if len(self.data) > 0:
            return self.data[-1]
        else:
            print("Stack empty")
            return None
    
    def size(self):
        return len(self.data)
    
    def TNprint(self):
        for node in self.data:
            if node:
                print (node.val)
            else:
                print(None)


class StackWMin():
    
    def __init__(self):
        self.data = []
        self.min = []
    
    def pop(self):
        if len(self.data) > 0:
            self.min.pop()
            return self.data.pop()
            
        else:
            print("Stack empty.")
            return
    
    def push(self, val):
        if len(self.data) == 0:
            self.min.append(val)
            return self.data.append(val)
        else:
            self.min.append(min(val,self.min[-1]))
            return self.data.append(val)
    
    def top(self):
        if len(self.data) > 0:
            return self.data[-1]
        else:
            print("Stack empty.")
            return None
    
    def min_(self):
        if len(self.data) > 0:
            return self.min[-1]
        else:
            print("Stack empty.")
            return None

#   --------------------------------------------------------------------------

class SetOfStacks():
    
    def __init__(self,maxSize):
        self.stackList = [myStack()]
        self.maxSize = maxSize
        self.indx = 0

    def push(self, val):
        if self.stackList[self.indx].size() < self.maxSize:
            self.stackList[self.indx].push(val)
        else:
            self.stackList.append(myStack())
            self.indx += 1
            self.stackList[self.indx].push(val)

    def pop(self):
        
        if self.stackList[self.indx].size() > 0:
            return self.stackList[self.indx].pop()
        else:
            if self.indx > 0:
                self.indx -= 1
                return self.stackList[self.indx].pop()
            else:
                print("Stack is empty. ")
                return None

    def popAt(self,j):
        if self.stackList[j].size() > 0:
            return self.stackList[j].pop()
        else:
            print("Stack is empty at index:", j)






    
    
        
          
        
        
        
    