import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
from batchsize import load_pickle_in_batches  # Import the function from batchsize.py

# Define a simple model
class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.flatten = nn.Flatten()
        self.fc1 = nn.Linear(28*28, 128)  # Update input dimensions as needed
        self.fc2 = nn.Linear(128, 10)
    
    def forward(self, x):
        x = self.flatten(x)
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

if __name__ == "__main__":
    model = SimpleNN()

    # Loss and optimizer
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    # Load data and train in batches
    file_path = 'C:/Users/rohit/OneDrive/Desktop/Research MBZUAI/2000_30_01.pickle'
    batch_size = 32  # Adjust the batch size as needed

    # Load dataset using DataLoader
    data = list(load_pickle_in_batches(file_path, batch_size))  # Load entire data into a list
    dataset = TensorDataset(torch.tensor(data))  # Convert to TensorDataset
    loader = DataLoader(dataset, batch_size=batch_size, shuffle=True)  # Create DataLoader

    # Training loop
    for batch in loader:
        inputs = batch[0]  # Assuming each batch contains inputs only
        optimizer.zero_grad()
        outputs = model(inputs)
        # Assuming targets are computed based on inputs or loaded separately
        targets = torch.randint(0, 10, (batch_size,))  # Replace with your actual targets
        loss = criterion(outputs, targets)
        loss.backward()
        optimizer.step()

        print(f'Loss: {loss.item()}')

    # Example code to evaluate the model (not shown here for brevity)
