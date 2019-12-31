from data_structures.graphs import *


def build_graph_savage_bfs():
    g = Graph()
    g.graph = {
        'r': ['s', 'v'],
        's': ['r', 'w'],
        't': ['u', 'w', 'x'],
        'u': ['t', 'y'],
        'v': ['r'],
        'w': ['s', 't', 'x'],
        'x': ['t', 'w', 'y'],
        'y': ['u', 'x']
    }
    return g


def build_graph_savage_dfs():
    g = Graph()
    g.graph = {
        1: [3, 5, 6, 9],
        2: [3, 4, 7],
        3: [1, 2, 4, 7, 9],
        4: [2, 3],
        5: [1, 7],
        6: [1],
        7: [2, 3, 5],
        8: [],
        9: [1, 3]
    }
    return g

