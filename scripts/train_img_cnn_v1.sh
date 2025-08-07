#! /usr/bin/bash

set -e

export WANDB_DISABLED=true
export WANDB_MODE=offline

repo_dir=$(dirname $(dirname $(realpath "$0")))
dp_dir="$repo_dir/diffusion_policy"

if [[ ! -f image_pusht_diffusion_policy_cnn.yaml ]]; then
    wget -O image_pusht_diffusion_policy_cnn.yaml https://diffusion-policy.cs.columbia.edu/data/experiments/image/pusht/diffusion_policy_cnn/config.yaml
fi

python $dp_dir/train.py \
    --config-dir=. \
    --config-name=image_pusht_diffusion_policy_cnn.yaml \
    training.seed=42 \
    training.device=cuda:0 \
    hydra.run.dir='data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}' \
    task.dataset.zarr_path=$repo_dir/data/pusht/pusht_cchi_v1.zarr \
    name=train_dp_cnn_img_v1 training.lr_scheduler=constant training.num_epochs=1000
