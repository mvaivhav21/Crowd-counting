import torch
x = torch.rand(3, 3)
print(x)
print(torch.cuda.is_available())  # Should return False if you installed the CPU-only version
