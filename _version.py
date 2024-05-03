__version__ = '2.0.2'

# 1.0.0 - Initial commit, added some structure files
# 1.1.0 - Added server.py and check_device.py
# 1.2.0 - Restructured the repository
# 1.2.1 - Created generate.py which now holds the code previously in the try block of the predict api call
# 1.2.2 - Created read_data.py which reads in our CSV file
# 1.3.0 - added functions to interact with database (insert data, get data)
# 1.3.1 - added create_jsonl.py to create a jsonl file with our data
# 1.3.2 - updated README
# 1.3.3 - updated create_jsonl.py to create train, test, and validation files
# 1.4.0 - have a first fine tuned model! Tuned using 800 iterations on an Apple Silicon Mac!
# 1.4.1 - added a directory and file for fine-tuning on eva and a requirements.txt for pip
# 1.5.0 - added files to fuse and upload fine-tuned models using mlx to huggingface
# 1.5.1 - added request.sh to make POST requests on EVA
# 1.5.2 - modified create_jsonl to include <eos> at the end of "text" and recreated train/test/valid.jsonl
# 1.6.0 - created an initial working fine-tuned model using Apple Silicon; video uploaded to Google Drive
# 1.6.1 - updated server_apple.py to work with adapters.npz
# 1.7.0 - create react app
# 1.7.1 - starting the react app build
# 1.8.0 - Created first working layout of frontend with API request ready for implementation
# 1.8.1 - adapter files for 800, 1600, 2400, 3200, 4000 iterations
# 1.8.2 - Some small edits to the frontend
# 1.8.3 - Modified server.py, server_apple.py, and created server_eva.py (to be worked on)
# 1.8.4 - Updated server files, should be better now
# 1.8.5 - Added Angora name
# 2.0.0 - Linked front end and back end (localhost)!
# 2.0.1 - Added and began a README for backend
# 2.0.2 - Updated main README