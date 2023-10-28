import torch
import time

# 设置使用GPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 创建两个28阶的张量
def create_tensors():
    tensor1 = torch.rand(*([2] * 28), dtype=torch.float32, device=device)
    tensor2 = torch.rand(*([2] * 28), dtype=torch.float32, device=device)
    return tensor1, tensor2

# 使用torch.tensordot收缩张量
def contract_with_tensordot(tensor1, tensor2):
    return torch.tensordot(tensor1, tensor2, dims=([i for i in range(15)], [i for i in range(15)]))

# 使用爱因斯坦积收缩张量
def contract_with_einsum(tensor1, tensor2):
    equation = ''.join([chr(97 + i) for i in range(28)]) + ',' + ''.join([chr(97 + i) for i in range(15)]) + ''.join([chr(97 + 15 + i) for i in range(13)]) + '->' + ''.join([chr(97 + i) for i in range(26)])
    return torch.einsum(equation, tensor1, tensor2)

# 主程序
def main():
    num_trials = 100

    # torch.tensordot的时间计算
    tensordot_times = []
    for _ in range(num_trials):
        tensor1, tensor2 = create_tensors()
        start_time = time.time()
        contract_with_tensordot(tensor1, tensor2)
        tensordot_times.append(time.time() - start_time)

    # 爱因斯坦积的时间计算
    einsum_times = []
    for _ in range(num_trials):
        tensor1, tensor2 = create_tensors()
        start_time = time.time()
        contract_with_einsum(tensor1, tensor2)
        einsum_times.append(time.time() - start_time)

    print(f"Average torch.tensordot time: {sum(tensordot_times):.5f} seconds")
    print(f"Average einsum time: {sum(einsum_times):.5f} seconds")

if __name__ == "__main__":
    main()
