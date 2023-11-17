import numpy as np
import time

# 生成两个24阶张量，每个维度为2
tensor1 = np.random.rand(*([2] * 24))  # 24个2维的张量
tensor2 = np.random.rand(*([2] * 24))  # 24个2维的张量

# 使用 tensordot 进行张量收缩，指定轴为共同的轴，并计时
start_time = time.time()
result_tensordot = np.tensordot(tensor1, tensor2, axes=24)
end_time = time.time()
tensordot_time = end_time - start_time

# 使用 einsum 进行张量收缩，指定收缩的指标，并计时
indices = ''.join(chr(ord('a') + i) for i in range(24))
einsum_expression = f"{indices},{indices}->"
start_time = time.time()
result_einsum = np.einsum(einsum_expression, tensor1, tensor2)
end_time = time.time()
einsum_time = end_time - start_time

# 打印结果和计时信息
print("tensordot result shape:", result_tensordot.shape)
print("einsum result shape:", result_einsum.shape)
print("tensordot time:", tensordot_time, "seconds")
print("einsum time:", einsum_time, "seconds")
