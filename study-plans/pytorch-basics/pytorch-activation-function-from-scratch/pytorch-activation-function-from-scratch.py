# import torch
# import math

# def activate(x: torch.Tensor, method: str = "relu") -> torch.Tensor:
#     """
#     Returns a float32 tensor with the same shape as x.
#     """
#     # pass
#     if method =="relu":
#         # return torch.maximum(torch.zeros_like(x),x)
#         # torch.relu(x)
#         return torch.clamp(x,min=0)
#     elif method == "sigmoid":
#         return (1+torch.exp(-x))**(-1)
#     elif method == "tanh":
#         return (torch.exp(x) - torch.exp(-x))/ (torch.exp(x) + torch.exp(-x))
#     elif method == "leakyrelu":
#         # return x if x>0 else 0.01*x
#         return torch.where(x>0,x,0.01*x)
# import torch

# def activate(x: torch.Tensor, method: str = "relu") -> torch.Tensor:
#     x = x.to(torch.float32)

#     if method == "relu":
#         return torch.relu(x)

#     elif method == "sigmoid":
#         return torch.sigmoid(x)

#     elif method == "tanh":
#         return torch.tanh(x)

#     elif method == "leakyrelu":
#         return torch.where(x > 0, x, 0.01 * x)

#     else:
#         raise ValueError(f"Unknown activation method: {method}")

import torch

def activate(x: torch.Tensor, method: str = "relu") -> torch.Tensor:
    """
    Returns a float32 tensor with the same shape as x.
    """
    if method == "relu":
        return torch.clamp(x, min=0)
    elif method == "sigmoid":
        return 1.0 / (1.0 + torch.exp(-x))
    elif method == "tanh":
        magnitude = torch.where(x >= 0, x, -x)
        decay = torch.exp(-2 * magnitude)
        positive = (1 - decay) / (1 + decay)
        return torch.where(x >= 0, positive, -positive)
    elif method == "leaky_relu":
        return torch.where(x > 0, x, 0.01 * x)