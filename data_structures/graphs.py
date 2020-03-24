#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 18:58:57 2019

@author: illuminatus
"""

from collections import defaultdict


class Graph:
    def __init__(self, directed=False):
        self.graph = defaultdict(list)
        self.directed = directed
        self.weights = dict()
    
    def add_vertex(self,v):
        self.graph[v] = []

    def add_edge(self, e, wt=1):
        vert, adjv = e
        if self.directed:
            if e not in self.weights:
                self.graph[vert].append(adjv)
            self.weights[e] = wt
        else:
            if e not in self.weights:
                self.graph[vert].append(adjv)
                self.graph[adjv].append(vert)
            self.weights[e] = wt
            self.weights[e[::-1]] = wt

    def create_from_edgelist(self, edges, weights=None):
        if weights:
            for e,w in zip(edges,weights):
                self.add_edge(e,w)
        else:
            for e in edges:
                self.add_edge(e)

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

    def dfs_node(self, node, top_sort, color, dfs_tree):

        color[node] = 'gray'
        for adjv in self.graph[node]:
            if color[adjv] is 'white':
                dfs_tree[adjv] = node
                self.dfs_node(adjv, top_sort, color, dfs_tree)
        color[node] = 'black'
        top_sort.append(node)

    def dfs(self, vs=None):
        dfs_tree = {}
        color = {v:'white' for v in self.graph.keys()}
        top_sort = []
        if not vs:
            vs = self.graph.keys()
        for v in vs:
            if color[v] is 'white':
                dfs_tree[v] = v
                self.dfs_node(v, top_sort, color, dfs_tree)
        return dfs_tree, top_sort[::-1]

    def transpose(self):
        gt = Graph(self.directed)
        for v in self.graph.keys():
            gt.add_vertex(v)
        es = self.edgelist()
        for e in es:
            w = self.weights[e]
            gt.add_edge(e[::-1],w)
        
        return gt

    def edgelist(self):
        if self.directed:
            return [(u,v) for u in self.graph.keys() for v in self.graph[u]]
        else:
            return [(u,v) for u in self.graph.keys() for v in self.graph[u] if u<v]



