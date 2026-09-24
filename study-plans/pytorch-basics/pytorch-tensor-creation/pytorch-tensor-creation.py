import torch

def create_tensor(method: str, shape: list, value: float = 0.0) -> torch.Tensor:
    """
    Returns a float32 tensor with the requested shape.
    """
    # pass
    if method =="zeros":
        return torch.zeros(shape)
    elif method == "ones":
        return torch.ones(shape)
    else:
        return torch.full(shape,value).to(torch.float32)