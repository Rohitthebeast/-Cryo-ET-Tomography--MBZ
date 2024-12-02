import torch
import torch.optim as optim
import torch.nn as nn
from torch.utils.data import DataLoader
from tqdm import tqdm
from dataset import CryoETPickleDataset, to_tensor  
from dualnet import DUALNet

def train_dual_net(model, dataloader, num_epochs=25, learning_rate=0.001):
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)
    
    for epoch in range(num_epochs):
        model.train()
        running_loss = 0.0
        for batch in tqdm(dataloader):
            noisy_imgs = batch['noisy']
            target_imgs = batch['target']
            noisy_imgs, target_imgs = noisy_imgs.to(device), target_imgs.to(device)  
            
            output = model(noisy_imgs)
            loss = criterion(output, target_imgs)
            
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            
            running_loss += loss.item()
        
        print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {running_loss/len(dataloader)}")

    return model

if __name__ == '__main__':
  
    device = torch.device("cpu")
    print(f"Using device: {device}")
    
    
    dataset = CryoETPickleDataset('C:/Users/rohit/OneDrive/Desktop/Research MBZUAI/2000_30_001.pickle', transform=to_tensor)
    dataloader = DataLoader(dataset, batch_size=4, shuffle=True, num_workers=4)
    
    
    dual_net = DUALNet().to(device)
    
    
    trained_model = train_dual_net(dual_net, dataloader, num_epochs=25)
