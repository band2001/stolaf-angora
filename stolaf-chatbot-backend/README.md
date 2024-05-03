# St. Olaf Angora Backend

This directory contains all the code used to host the Angora server as well as fine tune the model, including the datasets used for fine tuning.

## The Angora Server

Currently, the Angora server is a simple Flask app that accepts a post request with a user query and then sends back the models response. There are a few different versions of the server depending on which computer is hosting it. The Angora servers also use the 4000 iteration Angora model. You can optionally change the model to any of the other iterations if desired. 

### server_eva.py

Named after the EVA GPU machine at St. Olaf College, `server_eva.py` is intended to be run on a machine with NVIDIA GPUs and cuda configured. It follows the basic Google Gemma template for generation using the transformers library from HuggingFace. The transformer library approach is implemented in the `model_generate` function. This function can be found in algorithms/generate.py. To start the server, in the shell, use `python server_eva.py`. This server will run on port 8000.

To use server_eva.py, you will need to have torch, accelerate, transformers, flask, and flask_cors installed. 

### server_apple.py

This server should be used on Apple Silicon computers. This means on a Mac with an M-series chip. For the best performance it is recommended to be used on an Apple Max or Ultra chip with at least 24gb of RAM. As opposed to using the transformers library, to take advantage of the Apple Silicon hardware (both the GPUs and neural engine) the MLX library (mlx and mlx_lm) are utilized. The general approach is similar to the transformers library; however, it optimizes the hardware better. To start the server, in the shell, use `python server_apple.py`. This server will run on port 8000.

To use server_apple.py, you will need to have torch, accelerate, flask, flask_cors, mlx, and mlx_lm installed. 

### server_fastapi.py

WARNING: This server is still in development and has not been thoroughly tested. As opposed to the other servers using Flask, this server uses FASTAPI to improve the speed in making the request. However, development of this server was paused as it was discovered the majoritity of the bottlenecks in receiving a response in a timely fashion came down to the hardware being used to generate responses as opposed to the framework used to create the API. To run the FASTAPI server, the `run_fastapi.sh` file has the shell command to start it.

To use server_eva.py, you will need to have torch, accelerate, transformers, flask, and flask_cors installed. 

### server_generic.py

This was the original server used for testing. It is currently very similar to server_eva.py and is therefore not recommended for use at this time, instead use server_eva.py. 

To use server_eva.py, you will need to have torch, accelerate, transformers, flask, and flask_cors installed. 

### Helper Functions

`check_device.py`: checks whether you are using an Apple Silicon machine, an NVIDIA GPU machine with cuda, or neither (i.e. using the CPU).

`generate.py`: Generates a response from the fine tuned model given a query. This is done with the transformers library.

## Fine Tuning

Initially, the Angora models were meant to be trained on the EVA GPU machine (6 NVIDIA RTX 980 GPUs). However, given the 980 was released in 2014, there was not sufficient memory to actually load and fine tune the model using the bitsandbytes library. So, the Angora models were fine tuned using mlx and mlx_lm on an Apple Silicon machine. The `mlx-fine-tune` directory contains everything related to fine tuning Angora and the `eva-fine-tune` directory contains the code we used in an attempt to fine tune using NVIDIA and cuda. 

### MLX Fine Tuning

There are specific instructions for the process of fine tuning with mlx in the README in that directory. But the general idea is you can use various shell scripts to generate new weights for the fine tuned model, and then fuse it with an existing model (in this case Angora was fused with google/gemma-7b-it), and then upload it to HuggingFace.

With mlx fusing specifically, it does not format the tensors to have `metadata={"format":"pt"}`. If you are only using this model with mlx it does not matter, but if you want to use it with the transformers library you need to add it. To add it you either need to use format_safetensors.ipynb or change the library code for mlx_lm. From our experience, changing the library code for mlx_lm works best. The way to go about doing it is find the file {path to python libraries}/mlx_lm/utils.py and then replace the line `mx.save_safetensors(str(shard_path), shard, metadata={"format":"mlx"})` with `mx.save_safetensors(str(shard_path), shard, metadata={"format":"pt"})`. 

The adapter wieghts for each 800 iterations of fine tuning are included. So round1_adapters.npz corresponds to the 800 iteration Angora model, round5_adapters.npz corresponds to the 4000 iteration Angora model. 

Finally, if you would like to test your model with the fine tuned weights without loading it in from HuggingFace you can use `testing_ft_model.ipynb`.

### EVA Fine Tuning

This includes the code that can be used to fine tune on an NVIDIA cuda machine. When we tried to run it we ran out of RAM pretty quickly so cannot confirm how well it works or not. It uses a more traditional approach to fine tuning using bitsandbytes and quantizing the model. 

## Data

The data used to fine tune the model is in the data directory. It is included in a few formats: in a csv (`question_answer.csv`), in a SQLite database (`question_answer.db`), and in a jsonl file (`question_answer.jsonl`). The data directory has files with helper functions to manage reading in the data (from both the csv and database), initializing the database, and writing data to those various locations. One notable fill is the `create_jsonl.py` file with the `create_jsonl` function. This is used to create training, testing, and validation sets of the data and format them such that it follows the Google Gemma prompt template. That is why each entry in the datasets in the jsonl_data directory begin with `<bos><start_of_turn>...` and so forth. 