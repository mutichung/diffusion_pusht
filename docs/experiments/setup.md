## Hardware

- RTX A6000 (48GB)

## Reproducing the Results

First, make sure you have the environment activated.

```sh
mamba activate ./env
```

```sh
python scripts/train_state_transformer_v1.sh
python scripts/train_state_transformer_v2.sh
python scripts/train_img_cnn_v1.sh
python scripts/train_img_cnn_v2.sh
```
