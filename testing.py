import torch
from torch.utils.data import DataLoader
from dataset import CryoETPickleDataset, to_tensor
from dualnet import DUALNet
from cryocarenet import load_cryo_care_model

def apply_cryo_care(denoised_image, cryo_care_model):
    cryo_care_model.eval()
    with torch.no_grad():
        denoised_image = cryo_care_model(denoised_image)
    return denoised_image

if __name__ == '__main__':
    # Set device to CPU
    device = torch.device("cpu")
    print(f"Using device: {device}")
    
    # Load dataset
    dataset = CryoETPickleDataset('C:/Users/rohit/OneDrive/Desktop/Research MBZUAI/2000_30_001.pickle', transform=to_tensor)
    dataloader = DataLoader(dataset, batch_size=4, shuffle=False, num_workers=4)
    
    # Load trained DUALNet model
    dual_net = DUALNet().to(device)
    dual_net.load_state_dict(torch.load('path/to/your/trained_dual_net.pth', map_location=device))
    
    # Load the pretrained Cryo-CARE model
    cryo_care_model = load_cryo_care_model().to(device)
    
    # Example of post-processing an image using Cryo-CARE
    for batch in dataloader:
        noisy_imgs = batch['noisy'].to(device)
        with torch.no_grad():
            denoised_imgs = dual_net(noisy_imgs)
        
        # Apply Cryo-CARE post-processing
        final_denoised_imgs = apply_cryo_care(denoised_imgs, cryo_care_model)
        
        # Convert to numpy for visualization or further processing
        final_denoised_imgs_np = final_denoised_imgs.numpy()  # .cpu().numpy() not needed since already on CPU
