## Dependency Installation and Repository Setup

First, clone the repository.

```sh
git clone --recursive https://github.com/mutichung/diffusion_pusht.git
cd diffusion_pusht
```

The original author suggests using `mamba` or `conda` for environment creation.

```sh
mamba create -p ./env -f diffusion_policy/conda_environment.yaml
mamba activate ./env

# Pin version to avoid ImportError("cannot import name 'cached_download' from 'huggingface_hub'").
pip install huggingface_hub==0.11.1

# Uncomment this if you want to build the documentation.
# pip install mkdocs-material
```

## Patching and Installing `real-stanford/diffusion_policy`

> [!NOTE]
> The original `real-stanford/diffusion_policy` repository uses a flat layout instead of a more standard, `src`-based one. In addition, the `__init__.py` files are not presented in any subdirectories that contain python files [^1]. This makes it difficult to install the repository as a package using `pip install`. Therefore, I created the missing `__init__.py` files (plus some other changes) and save them as patches for others to use.

Apply the patches and install the repository as a package using the following commands.

```sh
git am patches/*
pip install -e diffusion_policy
```

[^1]: I suspect this is because the original author is using `hydra` for configuration management.

## Documentation

All documentation is written in plain markdown. MkDocs is used as the static site generator (SSG) to build the documentation. The theme used is Material for MkDocs.

To build it for deployment, run the following command.

```sh
pip install mkdocs-material
mkdocs build
```

The documentation is then available at `site/index.html`.
