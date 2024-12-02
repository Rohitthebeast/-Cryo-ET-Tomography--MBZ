# dual_net.py

import torch
import torch.nn as nn

class DUALNet(nn.Module):
    def __init__(self):
        super(DUALNet, self).__init__()
        self.encoder = nn.Sequential(
            nn.Conv3d(1, 64, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Conv3d(64, 128, kernel_size=3, padding=1),
            nn.ReLU()
        )
        self.decoder = nn.Sequential(
            nn.ConvTranspose3d(128, 64, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.ConvTranspose3d(64, 1, kernel_size=3, padding=1),
            nn.Sigmoid()
        )
    def forward(self, x):
        x = self.encoder(x)
        x = self.decoder(x)
        return x