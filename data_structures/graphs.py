#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 18:58:57 2019

@author: illuminatus
"""

from collections import defaultdict
import queue

class Graph:

    def __init__(self, directed=False):
        self.graph = defaultdict(list)
        self.directed = directed

    def add_edge(self, vert, adjv):
        if self.directed:
            self.graph[vert].append(adjv)
        else:
            self.graph[vert].append(adjv)
            self.graph[adjv].append(vert)

    def create_from_edgelist(self, edges):
        for e in edges:
            vert, adjv = e
            self.add_edge(vert, adjv)

    def create_from_adjlist(self, adjlist):
        self.graph = adjlist

    def __bfs_tree__(self, bfsq, visited, bfs_tree):
        while len(bfsq) > 0:
            vertex = bfsq.pop(0)
            for adjv in self.graph[vertex]:
                if visited[adjv] is False:
                    bfsq.append(adjv)
                    visited[adjv] = True
                    bfs_tree[adjv] = vertex

    def bfs(self):
        bfs_tree = {}
        visited = {v:False for v in self.graph.keys()}
        bfsq = []
        for v in self.graph.keys():
            if visited[v] is False:
                visited[v] = True
                bfsq.append(v)
                bfs_tree[v] = v
                self.__bfs_tree__(bfsq, visited, bfs_tree)
        return bfs_tree

    def __dfs_visit__(self, node, top_sort, color, dfs_tree):

        color[node] = 'gray'
        for adjv in self.graph[v]:
            if color[adjv] is 'white':
                dfs_tree[adjv] = node
                self.__dfs_visit__(adjv, top_sort, color, dfs_tree)
        color[node] = 'black'
        top_sort.append(node)

    def dfs(self):
        dfs_tree = {}
        color = {v: 'white' for v in self.graph.keys()}
        top_sort = []
        for v in self.graph.keys():
            if color[v] is 'white':
                dfs_tree[v] = v
                self.__dfs_visit__(v, top_sort, color, dfs_tree)
        return dfs_tree, top_sort

    def transpose(self):
        
        gt = Graph()
        for v in self.graph.keys():
            for av in self.graph[v]:
                gt.graph[av] = v
        
        return gt
