#!/zsh/sh

# pip3 install -U mlx mlx_lm transformers datasets

python3 -m mlx_lm.lora \
    --model ./mlx_gemma_7b_it \
    --train \
    --iters 800 \
    --data ../../data/jsonl_data \
    --resume-adapter-file ./round4_adapters.npz
    # --model google/gemma-2b-it \
