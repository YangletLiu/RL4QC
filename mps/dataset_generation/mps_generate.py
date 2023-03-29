import sys
sys.path.append('../..')
import numpy as np
from base import TensorNetwork
import os
import pickle


class MPS(TensorNetwork):
    def __init__(self, V):
        super().__init__(V)
    
    def build(self):
        for v in range(self.V-1):
            self.add_edge(v, v+1)
    
    def save(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self, f)
            
if __name__ == '__main__':
    V = 100
    mps = MPS(V)
    mps.build()
    mps.save('mps.pickle')
    with open('mps.pickle', 'rb') as f:
        mps2 = pickle.load(f)
    print("Number of tensor nodes: ", mps2.V)
    print("Number of edges: ",mps2.E)
    print("data structure: ",mps2.adj)