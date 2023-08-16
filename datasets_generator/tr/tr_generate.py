import opt_einsum as oe
import numpy as np
import math

def TR(n):
    n_dim_tensor = 3
    dim_tensor = 2
    tensor_shape = [[dim_tensor, dim_tensor, dim_tensor] for _ in range(n)]

    tensors = [np.random.rand(*shape) for shape in tensor_shape]

    # Build the enum string
    size_dict = {}
    possible_indices = [chr(i) for i in range(ord('a'), ord('z')+1)]
    possible_indices.extend([chr(i) for i in range(ord('A'), ord('Z')+1)])
    if n > 26:
        possible_indices.extend([chr(i + 140) for i in range(0, (n - 26) * 3)])


    str = '{}{}'.format(possible_indices[0], possible_indices[1])
    inputs = []
    last_index = 1
    inputs.append('{}{}'.format(possible_indices[0], possible_indices[1]))
    size_dict[possible_indices[0]] = 2
    size_dict[possible_indices[1]] = 2
    contracted_dim_index = [0]
    for i in range(1, n - 1):
        size_dict[possible_indices[last_index]] = 2
        size_dict[possible_indices[last_index + 1]] = 2
        size_dict[possible_indices[last_index + 2]] = 2
        str += ',{}{}{}'.format(possible_indices[last_index], possible_indices[last_index + 1],
                                possible_indices[last_index + 2])
        inputs.append('{}{}{}'.format(possible_indices[last_index], possible_indices[last_index + 1],
                                      possible_indices[last_index + 2]))
        contracted_dim_index.append(last_index + 1)
        last_index += 2


    str += ',{}{}{}'.format(possible_indices[last_index], possible_indices[last_index + 1],possible_indices[last_index + 2])
    inputs.append('{}{}{}'.format(possible_indices[last_index], possible_indices[last_index + 1],possible_indices[last_index + 2]))
    a, b = inputs[0][0], inputs[0][1]
    inputs[0] = [possible_indices[last_index + 2], a, b]
    contracted_dim_index.append(last_index + 1)
    size_dict[possible_indices[last_index + 2]] = 2
    str = '{}'.format(possible_indices[last_index + 2])+str
    # add string of all the possible indices
    str += '->'
    for i in range(len(contracted_dim_index)):
        str += possible_indices[contracted_dim_index[i]]
    return str

if __name__ == "__main__":
    for V in [4,5,6,7,8,9,10]:
        mps = TR(V)
        with open('/home/cxu-serve/p1/zzh136/zzh2023/quantum_data/tr/V_{}.txt'.format(V), 'w') as f:
            f.write(mps)