import torch
from fastapi import FastAPI, HTTPException
from transformers import AutoTokenizer, AutoModelForCausalLM
from pydantic import BaseModel


MODEL = "band2001/stolaf-angora-4000"

app = FastAPI()

class Query(BaseModel):
    prompt: str

def load_model(model_type = MODEL):
    global model
    global tokenizer

    tokenizer = AutoTokenizer.from_pretrained(model_type)
    model = AutoModelForCausalLM.from_pretrained(model_type, device_map="auto")

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

def model_generate(model, tokenizer, prompt):
    device = determine_device()

    input_ids = tokenizer(prompt, return_tensors="pt").to(device)

    outputs = model.generate(**input_ids, max_new_tokens=256)
    decoded_output =  tokenizer.decode(outputs[0])

    return decoded_output

app.post("/predict")
def generate(query: Query):
    try:
        if not query.prompt:
            raise HTTPException(status_code=400, detail="Request body did not contain a prompt key. Please include a prompt key with a string containing the request.")
        
        response = model_generate(model, tokenizer, query.prompt)

        return response

    except Exception as e:
        print(e)

    

if __name__ == "__main__":

    print("""Loading model and starting server...
          please wait until model is completely loaded""")
    
    load_model()