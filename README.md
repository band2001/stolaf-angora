# St. Olaf Angora

## Description
Angora is a chatbot fine tuned with the purpose of answering CS questions, included ones specific to St. Olaf. You can see the completed [Angora models on HuggingFace here](https://huggingface.co/collections/band2001/st-olaf-angora-6615fbbe61fb2574d52cafcb). This repository contains two primary directories, a directory for the frontend and a directory for the backend. The frontend is a React App and the backend contains the server files, files and code used to fine tune the model, and the data with helper functions. 

## Installation
Steps for installation are as follows:

### Backend:
1. Install required packages: 
    - pip install torch accelerate transformers flask flask_cors sqlite3 scikit-learn bitsandbytes fastapi
    - Note all of these are in the `requirements.txt` text file.
2. If you are using a Mac with an M series chip (Apple Silicon Mac), additionally install these packages:
    - pip3 install --pre torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/nightly/cpu
    - pip3 install mlx mlx_lm
3. Install huggingface hub to use the Gemma model:
    - pip install -U "huggingface_hub[cli]"
4. Login to Hugging face with your Access Token in Hugging face (found in the settings of profile)
    - Make sure you have access to the gemma model and have created an access token. The [Gemma model is found here](https://huggingface.co/google/gemma-7b) and the [Angora Models are found here](https://huggingface.co/collections/band2001/st-olaf-angora-6615fbbe61fb2574d52cafcb).
    - Type in terminal: huggingface-cli login
    - When prompted for Access Token, copy an Access Token from huggingface and paste to login
    - If prompted to allow access with github, say "Y"

You should now be ready to run any of the servers and explore the fine tuning methods used.

### Frontend

The frontend is a react project. Make sure you have node.js installed on your computer. Once you have node installed, in the frontend directory you can run `npm install` which will install all the necessary dependencies. Once those are installed, you can start using the front end!

## Usage
To use the chatbot, make sure you have a computer with appropriate hardware. This would be a machine with NVIDIA GPUs or an Apple Silicon Mac with a Max or Ultra chip. In the backend, start one of the servers. You can learn more about which server to choose in the README for the backend. The server will run on port 8000 of your machine. With the server running, in the front end directory use the command `npm start`. This will run the front end on port 3000 of your machine. You can now make queries and get a response!

For an example of the functioning chatbot, feel free to watch this [demo video](https://drive.google.com/file/d/1iwThVj88FTgLNANZdv2NineRcBXAqtZp/view?usp=sharing). 

## Authors
Ben Anderson & Keegan Murray, St. Olaf College

Special thanks to Sravya Kondrakunta for her support and guidance during the development process.

## License
Uses a MIT license.

## Project status
At this time project development has slowed down.
