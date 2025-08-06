---
draft: false
date: 2025-08-06
---

## Work Done

### Test Evaluation Script and Environment

Ran the evaluation command from `lerobot/diffusion_policy`.

```sh
python -m lerobot.scripts.eval --policy.path=lerobot/diffusion_pusht --output_dir ./output --env.type=pusht --eval.n_episodes=500 --eval.batch_size=50
```

And the results:

|                                   |  Mine | lerobot/diffusion_pusht | Paper |
| --------------------------------- | ----: | ----------------------: | ----: |
| Average max. overlap ratio        | 0.962 |                   0.955 | 0.957 |
| Success rate for 500 episodes (%) |  64.2 |                    65.4 |  64.2 |

### Dataset Discovery

I opened up a jupyter notebook playground and fiddled with the data a little bit. Here's the structure of the data with `zarr.open_group(path).tree()`:

```
/
├── data
│   ├── action (N, 2) float32
│   ├── img (N, 96, 96, 3) float32
│   ├── keypoint (N, 9, 2) float32
│   ├── n_contacts (N, 1) float32
│   └── state (N, 5) float32
└── meta
    └── episode_ends (K,) int64
```

Initiallly, I compared it to the `lerobot/pusht` dataset released by HuggingFace. However, the entries are so different that it's difficult to match them. I printed the arrays, displayed the images, trying to get a sense of what those values mean. Here's my attempt:

- `episode_ends` marks the ending scene/index of each episode. Use this to split the data into K rounds and label them with episode indices from 0 to K - 1.
- `state`: I make my assumptions by simultaneously looking at the corresponding image.
    - The first two numbers are the position of the tooltip.
    - 3rd & 4th are the positions of the T-shaped object.
    - 5th looks like the orientation of the object in radian.
- `img` visualizes the current state (potentially given the `keypoint`s and `state`s).

At some point I came up with the idea that I should also check the dataset released by the authors of the original paper. **BINGO**!

### `real-stanford/diffusion_policy`

Naturally, the next step is to discover the diffusion policy paper and code. Their README suggests running the notebook in colab, but I failed to open it due to some issues. I then turned to the example commands in the README.

I started with the low-dimension setup. Using the exact configuration from the paper, my results (0.944@750 and 0.948@950) seemed to match the authors' checkpoints. However, this is entirely based on the name of the checkpoint. Further investigation is required to determine whether this is a successful reproduction.

## WIP

- Reproducing both image and low-dimension experiments.
- Naively training on custom v1 dataset with only swapping the dataset itself.

## TODO

Focus on `real-stanford/diffusion_policy`.

- Look into colab notebooks.
- Training understanding
    - Policy input/output.
    - How is a diffusion model trained?
    - Hyperparameters.
- Evaluation understanding:
    - How do validation and test work?
    - Definition of metrics: success rate, reward.
- PushT environment: compare it to `lerobot/gym-pusht`.
- Data preprocessing
    - How image and low-dimension tasks utilize data.
    - Convert to lerobot-style dataset?
- Setup local `wandb`?
- Code cleanup and commit.

## Random Notes

### AttributeError: 'Space' object has no attribute 'add_collision_handler'

Looks like `pymunk` removed the method after version 7.0. Running `uv add 'pymunk<7'` solves the issue.

### Environment Preparation for `diffusion_policy`

Setting up the environment wasn't the easiest. This is a two-year-old project. Huggingface libraries have been moving fast and not afraid of breaking things. Python's dependency management via `conda` and `pip` isn't the best[^1]. All three factors lead to hours of fixing module/attribute not found errors and nonexistence of valid version combinations. Eventually, I had a fragile but working environment. Time for running some code!

[^1]: Let's hope for [uv](https://docs.astral.sh/uv/)!
