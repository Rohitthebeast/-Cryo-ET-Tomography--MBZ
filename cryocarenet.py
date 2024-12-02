

import torch
import torch.nn as nn

class CryoCARENet(nn.Module):
    def __init__(self):
        super(CryoCARENet, self).__init__()
        
    def forward(self, x):
        
        return x


def load_cryo_care_model():
    model = CryoCARENet()
    
    return model
