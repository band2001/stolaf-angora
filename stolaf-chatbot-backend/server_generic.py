import torch
import accelerate 
from transformers import AutoTokenizer, AutoModelForCausalLM
from flask import Flask, render_template, request
from flask_cors import CORS 
from algorithms.check_device import determine_device
from algorithms.generate import model_generate

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

model = None
tokenizer = None

def load_model(model_type = "band2001/stolaf-angora-4000"):
    global model
    global tokenizer

    tokenizer = AutoTokenizer.from_pretrained(model_type)
    model = AutoModelForCausalLM.from_pretrained(model_type, device_map="auto")

@app.route('/predict', methods=["GET", "POST"])
def predict():
    if request.method == 'POST':
        try: 
            decoded_output = model_generate(model, tokenizer, request)

            return decoded_output
        except:
            raise Exception("Error in model generation")
        

if __name__ == "__main__":

    print("""Loading model and starting server...
          please wait until model is completely loaded""")
    
    load_model()
    app.run(host="localhost", port=8000, debug=True)
