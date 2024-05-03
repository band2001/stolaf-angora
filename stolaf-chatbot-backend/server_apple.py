from mlx_lm import load, generate
from flask import Flask, request
from flask_cors import CORS 
# from algorithms.generate import model_generate

MODEL = "band2001/stolaf-angora-4000"

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

SYSTEM_PROMPT = '''You are very knowledgeable about computer science at St. Olaf College. You have a passion for helping answer computer science questions and troubleshoot issues for students. Your communication style is friendly, engaging, and informative, and you always strive to help students with their inquiries.

If a student asks about topics outside your area of expertise, such as medical advice or legal matters, politely inform them that you are not qualified to provide guidance on those subjects and suggest they consult with the appropriate professionals. If a user becomes hostile or uses inappropriate language, maintain a calm and professional demeanor, and remind them of the purpose and boundaries of your role as a computer science assistant at St. Olaf College.
'''

model = None
lora_model = None
tokenizer = None

def format_prompt(prompt, system_prompt = SYSTEM_PROMPT):

    return """<bos><start_of_turn>user
## Instructions
{}
## User
{}<end_of_turn>
<start_of_turn>model
""".format(system_prompt, prompt)

def model_generate(model, tokenizer, request):
    data = request.json

    prompt = format_prompt(data['prompt'])

    decoded_output = generate(
        model,
        tokenizer,
        prompt=prompt,
        verbose=True,
        temp=0.0,
        max_tokens=256,
    )

    return decoded_output

def load_model():
    global model
    global lora_model
    global tokenizer

    model, tokenizer = load(MODEL)
    
    # lora_model, _ = load(
    # "google/gemma-2b-it",
    # adapter_file="./algorithms/fine-tune-apple-silicon/adapters.npz",  # adapters.npz is the final checkpoint saved at the end of training
    # )

@app.route('/predict', methods=["GET", "POST"])
def predict():
    if request.method == 'POST':
        try: 
            decoded_output = model_generate(model, tokenizer, request)

            output = decoded_output.split("<",2)
            output = output[0]
            
            print(output)

            return output
        except Exception as exception:
            raise Exception(f"Error in model generation\n\n{exception}")
        

if __name__ == "__main__":

    print("""Loading model and starting server...
          please wait until model is completely loaded""")
    
    load_model()
    app.run(host="localhost", port=8000, debug=True)