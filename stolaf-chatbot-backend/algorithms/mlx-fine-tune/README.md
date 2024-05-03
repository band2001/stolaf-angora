# How to fine tune on Apple Silicon

## Setting up the data

The data needs to be split into train, test, and validation sets. It needs to be located in a directory where the only three files are train.jsonl, test.jsonl, and valid.jsonl.

## Fine Tuning the Model

Run mlx_lora.sh. Occasionally it fails, but if you have just restarted your Apple Silicon machine, it should run to completion. At the time of writing, it one sitting an M3 Max with the 30-core GPU and 36gb of RAM can do about 800 iterations before it runs out of resources.

## Fuse the base model with your fine tuning

Run mlx_fuse.sh. The uploading to huggingface part is commented out since it uploads only an mlx version of the safetensors which is incompatible with the transformers library.

## Change the safetensors to pt format

Run all the cells in format_safetensors.ipynb to convert the safetensors from mlx safetensors to pt safetensors so the model can be uploaded to huggingface and used with transformers.

## Upload the model to HuggingFace

Run mlx_upload.sh to upload to Huggingface.