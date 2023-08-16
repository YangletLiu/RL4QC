import sys
import numpy as np
import os
import pickle

def MPS(n):
    dim_tensor = 2 # size of each dimension, usually 2


    # generate random tensors
    tensor_shape = [[dim_tensor, dim_tensor, dim_tensor] for _ in range(n)]
    tensor_shape[0] = [dim_tensor, dim_tensor]
    tensor_shape[-1] = [dim_tensor, dim_tensor]
    tensors = [np.random.rand(*shape) for shape in tensor_shape]
    size_dict = {}
    # Build the enum string
    possible_indices = [chr(i) for i in range(ord('a'), ord('z')+1)]
    possible_indices.extend([chr(i) for i in range(ord('A'), ord('Z')+1)])
    possible_indices.extend([chr(i) for i in range(140, 140+n*3)])

    str = '{}{}'.format(possible_indices[0], possible_indices[1])
    last_index = 1
    size_dict[possible_indices[0]] = dim_tensor
    size_dict[possible_indices[1]] = dim_tensor
    contracted_dim_index = [0]
    for i in range(1, n-1):
        str += ',{}{}{}'.format(possible_indices[last_index], possible_indices[last_index+1], possible_indices[last_index+2])
        contracted_dim_index.append(last_index+1)
        size_dict[possible_indices[last_index]] = dim_tensor
        size_dict[possible_indices[last_index+1]] = dim_tensor
        size_dict[possible_indices[last_index+2]] = dim_tensor
        last_index += 2
    
    

    str += ',{}{}'.format(possible_indices[last_index], possible_indices[last_index+1])
    contracted_dim_index.append(last_index+1)
    size_dict[possible_indices[last_index]] = dim_tensor
    size_dict[possible_indices[last_index+1]] = dim_tensor
    inputs = str
    return inputs
            
if __name__ == '__main__':
    for V in [100, 200, 300, 400, 500,600,700,800,900,1000]:
        mps = MPS(V)
        with open('/home/cxu-serve/p1/zzh136/zzh2023/quantum_data/mps/V_{}.txt'.format(V), 'w') as f:
            f.write(mps)
    # with open('mps.pickle', 'rb') as f:
    #     mps2 = pickle.load(f)
    # print("Number of tensor nodes: ", mps2.V)
    # print("Number of edges: ",mps2.E)
    # print("data structure: ",mps2.adj)