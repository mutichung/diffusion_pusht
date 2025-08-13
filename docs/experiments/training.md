## Overview

Training is mainly done via the `train.py` script from `real-stanford/diffusion_policy`. Minor modifications are made to the training configuration to match the experimental settings described in the paper, and can be found in the corresponding shell scripts.

```sh
python scripts/train_lowdim_transformer_v1.sh
python scripts/train_lowdim_transformer_v2.sh
python scripts/train_img_cnn_v1.sh
python scripts/train_img_cnn_v2.sh
python scripts/train_lowdim_cnn_v1.sh
python scripts/train_lowdim_cnn_v2.sh
```

## Hardware

- RTX A6000
