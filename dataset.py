import pickle
import torch
from torch.utils.data import Dataset

class CryoETPickleDataset(Dataset):
    def __init__(self, file_path, transform=None):
        self.file_path = file_path
        self.transform = transform

        with open(file_path, 'rb') as handle:
            self.data = pickle.load(handle, encoding='latin1')  # Specify the correct encoding

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        sample = self.data[idx]
        if self.transform:
            sample = self.transform(sample)
        return sample

def to_tensor(sample):
    return torch.tensor(sample, dtype=torch.float32)

def normalize(sample):
    sample -= sample.min()
    sample /= sample.max()
    return sample
