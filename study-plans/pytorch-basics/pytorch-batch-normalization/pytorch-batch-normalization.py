import torch

def batch_norm(X: torch.Tensor, gamma: torch.Tensor, beta: torch.Tensor, eps: float = 1e-5) -> torch.Tensor:
    """
    Returns a float32 tensor with the same shape as X.
    """
    # pass
    mean = X.mean(dim=0,keepdim=True)
    sigma = (X-mean).pow(2).mean(dim=0,keepdim=True)
    Y = gamma * ((X-mean)/(sigma+eps).pow(0.5)) + beta

    return Y
    
