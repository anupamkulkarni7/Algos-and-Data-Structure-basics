#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 18:58:57 2019

@author: illuminatus
"""

from collections import defaultdict
import queue

#-----------------------------------------------------------------------------
class Graph:
#-----------------------------------------------------------------------------
    
    def __init__(self):
        self.graph = defaultdict(list)

    
    def addEdge(self,vert,adjv):
        self.graph[vert].append(adjv)
     
#   ---------------------------------------------
        
    def __BFStree__(self,p,q,visited):        
        while q.empty() == False:
            v = q.get()
            for adjv in self.graph[v]:
                if visited[adjv] == False:
                    p[adjv] = v
                    q.put(adjv)
                    visited[adjv] = True
                   
    def BFS(self):       
        visited = {}
        for v in self.graph.keys():
            visited[v] = False
        
        p = {}
        q = queue.Queue(len(self.graph.keys()))
        
        for v in self.graph.keys():
            if visited[v] == False:
                visited[v] = True
                q.put(v)
                p[v] = v
                self.__BFStree__(p,q,visited)
        
        return p
    
#   ---------------------------------------------    
    
    def __DFSvisit__(self,v,color,p):
        
        color[v] = 'Gray'
        for u in self.graph[v]:
            if color[u] == 'White':
                p[u] = v
                self.__DFSvisit__(u,color,p)
        
        color[v] = 'Black'
    
    def DFS(self):
        
        color={}
        for v in self.graph.keys():
            color[v] = 'White'
        
        p = {}
        for v in self.graph.keys():
            if color[v] == 'White':
                self.__DFSvisit__(v,color,p)
        
        return p

#   ---------------------------------------------  
    def transpose(self):
        
        gt = Graph()
        for v in self.graph.keys():
            for av in self.graph[v]:
                gt.graph[av] = v
        
        return gt
        

#----------------------------------------------------------------------------- 
#End of Graph definitions
#-----------------------------------------------------------------------------    

def buildGraph1(a):
    a.addEdge(1,2); a.addEdge(1,5)
    a.addEdge(2,1); a.addEdge(2,6)
    a.addEdge(3,4); a.addEdge(3,6); a.addEdge(3,7)
    a.addEdge(4,3); a.addEdge(4,8)
    a.addEdge(5,1)
    a.addEdge(6,2); a.addEdge(6,3); a.addEdge(6,7)
    a.addEdge(7,3); a.addEdge(7,6); a.addEdge(7,8)
    a.addEdge(8,4); a.addEdge(8,7)
    #return a

def buildGraph2(a):
    
    a.addEdge(1,3); a.addEdge(1,5); a.addEdge(1,6); a.addEdge(1,9)
    a.addEdge(2,3); a.addEdge(2,4); a.addEdge(2,7)
    a.addEdge(3,1); a.addEdge(3,2); a.addEdge(3,4); a.addEdge(3,7); a.addEdge(3,9)
    a.addEdge(4,2); a.addEdge(4,3)
    a.addEdge(5,1); a.addEdge(5,7)
    a.addEdge(6,1)
    a.addEdge(7,2); a.addEdge(7,3); a.addEdge(7,5)
    a.addEdge(8,8)
    a.addEdge(9,1); a.addEdge(9,3)


def main():
    a = Graph()
    buildGraph2(a)
    """
    a.graph = {'r':['s','v'],
            's':['r','w'],
            't':['u','v'],
            'u':['t','y'],
            'v':['r'],
            'w':['s','t','x'],
            'x':['t','w','y'],
            'y':['u','x']}
    """
    
    #at = a.transpose()    
    ans = a.DFS()
    print(ans)
       
if __name__ == '__main__':
    main()