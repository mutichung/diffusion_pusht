To evaluate the results, run the following command.

```sh
python scripts/eval.py --exp PATH_TO_OUTPUT
```

| Observation | Dataset | Model       | Mean Score | Success Rate | Time Taken |
|-------------|---------|-------------|-----------:|-------------:|-----------:|
| State       | v1      | Transformer |     0.8329 |       0.7980 |     6h 17m |
| State       | v2      | Transformer |     0.9472 |       0.8800 |     6h 55m |
| Image       | v1      | CNN         |     0.7995 |       0.5540 |    31h 52m |
| Image       | v2      | CNN         |     0.8329 |       0.6680 |    41h 05m |
