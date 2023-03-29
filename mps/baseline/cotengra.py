
import opt_einsum as oe
import cotengra as ctg
import numpy as np
import math

n=10 # number of tensors
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
# add string of all the possible indices
output = ''
for i in range(len(contracted_dim_index)):
    output += possible_indices[contracted_dim_index[i]]

opt = ctg.HyperOptimizer(
    minimize='flops',
    reconf_opts={},
    progbar=True,
)
tree = opt.search(inputs, output, size_dict)

