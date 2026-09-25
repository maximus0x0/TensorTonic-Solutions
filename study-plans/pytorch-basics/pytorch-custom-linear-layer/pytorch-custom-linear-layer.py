import torch
import torch.nn as nn

torch.manual_seed(42)

class CustomLinear(nn.Module):
    def __init__(self, in_features: int, out_features: int):
        super().__init__()
        # pass
        # self.nn.parameters()
        self.weight = nn.Parameter(
            torch.randn(out_features,in_features)
        )
        self.bias = nn.Parameter(
            torch.randn(out_features)
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Returns a float32 tensor of shape (batch, out_features).
        """
        # pass
        # # torch.randn()
        # w = torch.randn(in_features,out_features)
        # b = torch.randn(out_features,)
        return x @ self.weight.T + self.bias
