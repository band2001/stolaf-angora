from algorithms.check_device import determine_device

def model_generate(model, tokenizer, request):
    device = determine_device()
    print(device)     
    data = request.json

    input_ids = tokenizer(data["prompt"], return_tensors="pt").to(device)

    outputs = model.generate(**input_ids, max_length = 40)
    decoded_output =  tokenizer.decode(outputs[0])

    return decoded_output