python3 -m mlx_lm.fuse \
    --model google/gemma-7b-it \
    --adapter-file round2_adapters.npz \
    # --upload-repo band2001/gg2bit-stolaf-chatbot-mlx-v0.1 \
    # --hf-path google/gemma-2b-it