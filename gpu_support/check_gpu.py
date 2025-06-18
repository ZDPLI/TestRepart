import torch

def has_cuda():
    return torch.cuda.is_available()

if __name__ == '__main__':
    print('CUDA available' if has_cuda() else 'CUDA not available')
