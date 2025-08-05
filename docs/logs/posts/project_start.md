---
draft: false
date: 2025-08-05
---

## Work Done

- Watched the youtube video of [diffusion policy presentation](https://www.youtube.com/watch?v=M03sZFfW-qU). My takeaways:
    - Human's vision reaction time is ~300ms. If the training data is collected by human, each action sequence/chunk should be at the same order of magnitudes to that[^1].
    - Diffusion policy works well both in joint-space and action-space. However, working in action space requires a good IK.
- Created repository.
- Draft plan:
    - `huggingface/lerobot`: start from the training and evaluation scripts there. Maybe reproduce [`lerobot/diffusion_pusht`](https://huggingface.co/lerobot/diffusion_pusht) if feasible.
    - Per request, use [`huggingface/gym-pusht`](https://github.com/huggingface/gym-pusht) for simulation environment.
    - Maybe [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) for documentation and report.
      - Or maybe just the paper-style, good-old $\LaTeX$.
    - `uv` for package management? Not sure if this would work since most of the environment requires `conda`/`mamba` for non-python dependencies.
    - `marimo` or `jupyter notebook` for interactive sessions? Or use the jupyter notebook extension for mkdocs.

## TODO

- Understand difference between DDPM and DDIM[^2].
- Fiddle with `lerobot/diffusion_pusht`.
    - Understand the workflow.
    - Get a feeling of how resource-hungry are the training & evaluation scripts.
- Discover the custom pusht dataset.
- Perhaps read the paper?

[^1]: During the Q&A session at [51:18](https://youtu.be/M03sZFfW-qU?si=NLt29RcZSu__XZ9b&t=3078)
[^2]: Mentioned during the [final Q&A](https://youtu.be/M03sZFfW-qU?si=uNDlh4rILe9zsLXC) regarding speed optimizations.
