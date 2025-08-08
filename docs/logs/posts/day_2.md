---
draft: false
date: 2025-08-07
---

## Work Done

### Training with `real-stanford/diffusion_policy`

Ran two experiment setups using the `real-stanford/diffusion_policy` repository.

1. Transformer + state-based observations.
2. UNet + image-based observations.

Both configurations were trained on two datasets, making a 2x2 matrix. Most default settings were adopted, except for the number of epochs and learning rate scheduler. The number fo epochs was set to 1000 for all cases in order to get a quick taste, and the learning rate scheduler is set to constant to make sure the model goes far enough.

> Insert table

#### Analysis

Interestingly, models trained on dataset v1 both outperformed the ones trained on dataset v2. Dataset v2 is roughly double the size of v1, thus I initially thought scaling law would also work. Two potential reasons:

- Quality in data: maybe v2 yields lower quality?
- Larger dataset requires longer training time.

On the other hand, state-based model outperforms image-based model. I think this is expected since intuitively there definitely will be estimation errors when using vision.

## WIP

- Still fighting with environment setup 😢.
    - Currently maintaining two environments: one for `diffusion_policy`, the other for my repository.
- Change of plan again.
    - Don't want to fork `diffusion_policy` $\to$ temporarily use git submodule instead for reproduction purposes.
    - Tried to install `diffusion_policy` with `pip` or `conda` but have no luck. The *flat* layout and the lack of `__init__.py` prohibited me from importing it as a module.
    - Colab notebook is almost a self-contained training + evaluation code. Adopt that but instead structure it into a `tiny_dp` python submodule.

## TODO

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
