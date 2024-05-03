import torch

def determine_device(): 
    local_device = None
    try:
        if(torch.backends.mps.is_available()): # for Apple Silicon Macs
            local_device = "mps"
        elif(torch.cuda.is_available()): # for NVIDA GPUs (can use Cuda)
            local_device = "cuda"
        else:
            local_device = "auto"
        return local_device
    except:
        raise Exception("Error determining device GPU, do you have Torch Preview installed?")