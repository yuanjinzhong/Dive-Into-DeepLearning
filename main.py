import sys
import numpy
import scipy
import torch

x = torch.arange(12)


if __name__ == "__main__":
    print(numpy.__version__)
    print(scipy.__version__)
    print(sys.version)
    print(x)
    print(x.shape)
    print(x.numel())
    print(x.shape)
