#! /usr/bin/bash

set -e

export WANDB_DISABLED=true
export WANDB_MODE=offline

repo_dir=$(dirname $(dirname $(realpath "$0")))
dp_dir="$repo_dir/diffusion_policy"

python $dp_dir/train.py \
    --config-dir=$dp_dir \
    --config-name=train_diffusion_transformer_lowdim_pusht_workspace.yaml \
    training.seed=42 \
    training.device=cuda:0 \
    hydra.run.dir='data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}' \
    task.dataset.zarr_path=$repo_dir/data/pusht/pusht_cchi_v2.zarr \
    name=train_dp_transformer_lowdim_v2 training.num_epochs=4500 \
    checkpoint.topk.k=10 \
    checkpoint.topk.monitor_key=epoch
