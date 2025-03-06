import torch

print("PyTorch version:", torch.__version__)

# 创建两个随机张量
x = torch.rand(3, 3)
y = torch.rand(3, 3)
print("Tensor x:")
print(x)
print("Tensor y:")
print(y)

# 执行张量加法
z = x + y
print("Tensor x + y:")
print(z)

# 检查 CUDA 是否可用，并在 GPU 上运行示例
if torch.cuda.is_available():
    print("CUDA is available! Running on GPU.")
    x_cuda = x.to("cuda")
    y_cuda = y.to("cuda")
    z_cuda = x_cuda + y_cuda
    print("Tensor x + y on GPU:")
    print(z_cuda)
else:
    print("CUDA is not available. Running on CPU.")
