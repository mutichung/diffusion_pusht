---
draft: true
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

## Random Notes

### AttributeError: 'Space' object has no attribute 'add_collision_handler'

Looks like `pymunk` removed the method after version 7.0. Running `uv add 'pymunk<7'` solves the issue.
