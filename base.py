import numpy as np

class TensorNetwork():
    def __init__(self, V):
        self.V = V
        self.E = 0
        self.adj = [[] for _ in range(V)]
    
    def add_edge(self, u, v):
        if u>v: u,v = v,u
        self.adj[u].append(v)
        self.E += 1
    
    def build(self, *args, **kwargs):
        raise NotImplementedError
    
    def save(self, filename):
        raise NotImplementedError