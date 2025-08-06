#! /usr/bin/bash

python -m lerobot.scripts.eval \
    --policy.path=lerobot/diffusion_pusht \
    --output_dir ./outputs \
    --env.type=pusht \
    --eval.n_episodes=500 \
    --eval.batch_size=50
