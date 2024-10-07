FROM paperspace/gradient-base:pt211-tf215-cudatk120-py311-20240202

# RUN python3 -m pip --no-cache-dir install --upgrade torch==2.4.1 torchvision==0.19.1 torchaudio==2.4.1 --extra-index-url https://download.pytorch.org/whl/cu121

RUN python3 -m pip --no-cache-dir install --upgrade transformers datasets peft tokenizers accelerate diffusers safetensors

RUN python3 -m pip --no-cache-dir install --upgrade bitsandbytes tqdm wandb

EXPOSE 8888 6006

CMD jupyter lab --allow-root --ip=0.0.0.0 --no-browser --ServerApp.trust_xheaders=True --ServerApp.disable_check_xsrf=False --ServerApp.allow_remote_access=True --ServerApp.allow_origin='*' --ServerApp.allow_credentials=True