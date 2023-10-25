import torch
import time
import numpy as np

# 设置设备为CPU
device_cpu = torch.device("cpu")

# 创建两个25阶的复数张量，每一阶的维度为2，数据类型为复数
real_part_cpu = np.random.rand(*([2] * 25)).astype(np.float32)
imag_part_cpu = np.random.rand(*([2] * 25)).astype(np.float32)
signs_cpu = np.random.choice([1, -1], size=real_part_cpu.shape)
real_cpu = torch.tensor(real_part_cpu, dtype=torch.float32, device=device_cpu)
imag_cpu = torch.tensor(signs_cpu * imag_part_cpu, dtype=torch.float32, device=device_cpu)
complex_tensor1_cpu = torch.complex(real_cpu, imag_cpu)

real_part_cpu = np.random.rand(*([2] * 25)).astype(np.float32)
imag_part_cpu = np.random.rand(*([2] * 25)).astype(np.float32)
signs_cpu = np.random.choice([1, -1], size=real_part_cpu.shape)
real_cpu = torch.tensor(real_part_cpu, dtype=torch.float32, device=device_cpu)
imag_cpu = torch.tensor(signs_cpu * imag_part_cpu, dtype=torch.float32, device=device_cpu)
complex_tensor2_cpu = torch.complex(real_cpu, imag_cpu)

# 创建两个25阶的复数张量，每一阶的维度为2，数据类型为复数，位于GPU上
device_gpu = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

real_part_gpu = np.random.rand(*([2] * 25)).astype(np.float32)
imag_part_gpu = np.random.rand(*([2] * 25)).astype(np.float32)
signs_gpu = np.random.choice([1, -1], size=real_part_gpu.shape)
real_gpu = torch.tensor(real_part_gpu, dtype=torch.float32, device=device_gpu)
imag_gpu = torch.tensor(signs_gpu * imag_part_gpu, dtype=torch.float32, device=device_gpu)
complex_tensor1_gpu = torch.complex(real_gpu, imag_gpu)

real_part_gpu = np.random.rand(*([2] * 25)).astype(np.float32)
imag_part_gpu = np.random.rand(*([2] * 25)).astype(np.float32)
signs_gpu = np.random.choice([1, -1], size=real_part_gpu.shape)
real_gpu = torch.tensor(real_part_gpu, dtype=torch.float32, device=device_gpu)
imag_gpu = torch.tensor(signs_gpu * imag_part_gpu, dtype=torch.float32, device=device_gpu)
complex_tensor2_gpu = torch.complex(real_gpu, imag_gpu)

# 执行张量收缩运算在CPU上
start_time_cpu = time.time()
result_tensor_cpu = torch.tensordot(complex_tensor1_cpu, complex_tensor2_cpu, dims=([0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                                                                                     10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
                                                                                     20, 21, 22, 23, 24],
                                                                                    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                                                                                     10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
                                                                                     20, 21, 22, 23, 24]))
end_time_cpu = time.time()

# 计算CPU运行时间
execution_time_cpu = end_time_cpu - start_time_cpu

# 设置CUDA事件来记录GPU的数据传输和计算时间
start_event = torch.cuda.Event(enable_timing=True)
end_event = torch.cuda.Event(enable_timing=True)

# 记录数据传输的开始时间
start_event.record()

# 执行张量收缩运算在GPU上（基础版本）
start_time_gpu = time.time()
result_tensor_gpu = torch.tensordot(complex_tensor1_gpu, complex_tensor2_gpu, dims=([0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                                                                                     10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
                                                                                     20, 21, 22, 23, 24],
                                                                                    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                                                                                     10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
                                                                                     20, 21, 22, 23, 24])).to(device_gpu)
end_time_gpu = time.time()

# 记录数据传输的结束时间
end_event.record()
end_event.synchronize()

# 计算GPU数据传输时间
data_transfer_time_gpu = start_event.elapsed_time(end_event)

# 计算GPU计算时间
gpu_computation_time_gpu = end_time_gpu - start_time_gpu

# 打印CPU运行结果和时间
print("CPU运行时间（秒）：", execution_time_cpu)

# 打印基础GPU版本的运行结果和时间
print("基础GPU运行时间（毫秒）：", data_transfer_time_gpu + gpu_computation_time_gpu)
print("基础GPU计算时间（毫秒）：", gpu_computation_time_gpu)
print("基础GPU数据传输时间（毫秒）：", data_transfer_time_gpu)

# 打印分隔线，表示强化版本GPU计算时间的开始
print("-------- 强化版本GPU计算时间 --------")


# 优化GPU版本的并行操作
def optimized_gpu_tensordot(a, b):
    # 将张量分成多块并行计算
    num_chunks = 8  # 可根据GPU性能进行调整
    chunk_size = a.shape[0] // num_chunks
    results = []
    computation_times = []
    transfer_times = []
    for i in range(num_chunks):
        start_idx = i * chunk_size
        end_idx = start_idx + chunk_size
        chunk_a = a[start_idx:end_idx]
        chunk_b = b[start_idx:end_idx]

        # 记录数据传输的开始时间
        start_event.record()

        result_chunk = torch.tensordot(chunk_a, chunk_b, dims=([0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                                                                10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
                                                                20, 21, 22, 23, 24],
                                                               [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                                                                10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
                                                                20, 21, 22, 23, 24])).to(device_gpu)

        # 记录数据传输的结束时间
        end_event.record()
        end_event.synchronize()

        # 计算数据传输时间
        transfer_time = start_event.elapsed_time(end_event)

        results.append(result_chunk)
        computation_times.append(end_time_gpu - start_time_gpu)
        transfer_times.append(transfer_time)

    # 返回结果列表，计算时间列表和数据传输时间列表
    return results, computation_times, transfer_times


# 使用强化版本的GPU执行张量收缩运算
start_time_gpu_optimized = time.time()
result_tensor_gpu_optimized_chunks, computation_times_optimized, transfer_times_optimized = optimized_gpu_tensordot(
    complex_tensor1_gpu, complex_tensor2_gpu)
end_time_gpu_optimized = time.time()

# 汇总强化版本GPU的结果
result_tensor_gpu_optimized = torch.sum(torch.stack(result_tensor_gpu_optimized_chunks), dim=0)

# 计算强化版本GPU的计算时间
gpu_optimized_computation_time = end_time_gpu_optimized - start_time_gpu_optimized

# 计算强化版本GPU的数据传输时间
gpu_optimized_data_transfer_time = sum(transfer_times_optimized)

# 打印强化版本GPU的运行时间
print("强化版本GPU运行时间（毫秒）：", gpu_optimized_computation_time + gpu_optimized_data_transfer_time)
print("强化版本GPU计算时间（毫秒）：", gpu_optimized_computation_time)
print("强化版本GPU数据传输时间（毫秒）：", gpu_optimized_data_transfer_time)

# 打印分隔线，表示数据传输时间的开始
print("-------- 数据传输时间 --------")

# 打印GPU优化版本的数据传输时间
for i in range(len(transfer_times_optimized)):
    print(f"计算块 {i + 1} - 数据传输时间（毫秒）：{transfer_times_optimized[i]}")

# 打印结果张量形状（强化版本GPU）
print("结果张量形状（强化版本GPU）：", result_tensor_gpu_optimized.shape)