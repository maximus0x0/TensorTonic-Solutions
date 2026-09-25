import torch
import torch.nn as nn

class SimpleNet(nn.Module):
    def __init__(self, in_features: int, hidden_size: int, out_features: int):
        super().__init__()
        # pass
        self.Linear1 = nn.Linear(in_features,hidden_size)
        self.Linear2 = nn.Linear(hidden_size,out_features)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Returns a float32 tensor of shape (batch, out_features).
        """
        # pass
        # self.Linear1 = nn.Linear(in_features,hidden_size)
        return self.Linear2(torch.relu(self.Linear1(x)))

        