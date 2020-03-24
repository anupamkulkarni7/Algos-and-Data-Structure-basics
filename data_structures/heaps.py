#!/usr/bin/env python3

import sys


class MinHeap:
    def __init__(self):
        self.count = 0
        self.array = [] #Store [key,value] pairs as a list
        self.pos = dict()

    def get_min(self):
        return self.array[0][::-1]

    def heapify_up(self,i):
        if i is 0:
            return
        par = (i-1)//2
        if self.array[i][1] < self.array[par][1]:
            self.array[i], self.array[par] = self.array[par], self.array[i]
            self.pos[self.array[i][0]] = i
            self.pos[self.array[par][0]] = par
            self.heapify_up(par)
        else:
            return

    def heapify_down(self,i=0):
        if i > (self.count//2 - 1): #ie. leaf
            return
    
        lc = 2*i + 1
        rc = 2*i + 2
        if rc >= self.count:
            child = lc
        else:
            if self.array[lc][1] < self.array[rc][1]:
                child = lc
            else:
                child = rc

        if self.array[i][1] > self.array[child][1]:
            self.array[i],self.array[child] = self.array[child], self.array[i]
            self.pos[self.array[i][0]] = i
            self.pos[self.array[child][0]] = child
            self.heapify_down(child)
        else:
            return

    def insert(self,item):
        k, v = item
        if k in self.pos:
            print("Key already exists.")
            return 
        self.array.insert(self.count,[k,v])
        self.pos[k] = self.count
        self.count += 1
        self.heapify_up(self.pos[k])

    def extract_min(self, remove=True):
        if self.count is 0:
            return None
        self.array[0], self.array[self.count-1] = self.array[self.count-1], self.array[0]
        self.pos[self.array[0][0]] = 0
        del self.pos[self.array[self.count-1][0]]
        self.count -= 1
        
        self.heapify_down()

        if remove:
            return self.array.pop()
        else:
            return self.array[self.count]
     
    def decrease_key(self, key, val):
        if key not in self.pos:
            print("Key not found.")
            return
        i = self.pos[key]
        self.array[i][1] = val
        self.heapify_up(i)
    
    def delete(self, key):
        self.decrease_key(key, -sys.maxsize)
        _,_ = self.extract_min(remove=True)

    def build_heap(self,arr):
        if self.count is not 0:
            print("Use empty heap.")
            return

        """
        self.count = len(arr)
        last_node = (self.count//2) - 1
        self.pos = {v[0]:i for i,v in enumerate(arr)}
        self.array = arr[:]
        for i in range(last_node,-1,-1): #loop over non-leaf nodes
            self.heapify_down(i)
        """
        for k,v in arr:
            self.insert([k,v])

    def is_empty(self):
        return self.count is 0

    def get_value(self,key):
        return self.array[self.pos[key]][1]

