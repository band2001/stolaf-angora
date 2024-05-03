#!/zsh/sh

# pip3 install -U mlx mlx_lm transformers datasets

python3 -m mlx_lm.lora \
    --model ./mlx_gemma_7b_it \
    --data ../../data/jsonl_data \
    --adapter-file ./round5_adapters.npz \
    --test
    # --model google/gemma-2b-it \
