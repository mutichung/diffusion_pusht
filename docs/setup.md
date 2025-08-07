First, clone the repository.

```sh
git clone --recursive https://github.com/mutichung/diffusion_pusht.git
cd diffusion_pusht
```

I have two virtual environments. One for reproducing the results from the original paper using their codebase.

## Environment Setup for `real-stanford/diffusion_policy`

The original author suggests using `mamba` or `conda` for environment creation.

```sh
mamba create -p ./env -f diffusion_policy/conda_environment.yaml
mamba activate ./env

# Pin version to avoid ImportError("cannot import name 'cached_download' from 'huggingface_hub'").
pip install huggingface_hub==0.11.1
```
