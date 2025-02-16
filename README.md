# Automated chemical synthesis in the aerosol phase
This repository contains both

* MicroPython code for automated execution of experiments on our *Aeroboard* hardware
* A Jupyter notebook for analyzing microscope images of the experiments, including image segmentation to find the location and sizes of droplets as well as statistical analysis to 

## MicroPython code
The MicroPython code is located in the `lib` and `experiments` folders. The `lib` folder contains the `CtrlAer` library, described in a separate paper ([10.36227/techrxiv.173896967.76043093/v1]). The `experiments` folder contains  scripts for running the automated aerosol experimental procedures described in the paper.

To run the experiments, copy the contents of the `lib` and `experiments` folders to the using the Thonny IDE or the `rshell` tool. The exact GPIO pins used for the peripherals may need to be adjusted in the scripts depending on your specific board and circuit configuration. The default values are optimised for execution on the *AeroBoard*.

## Jupyter notebook
The Jupyter notebook `particle_stats.ipynb` is used for analyzing microscope images of the experiments. The code in this repository has only been tested on Linux (x86-64) using Python 3.10 and can be run by following the manual steps below or by using the dev container, e.g. in Visual Studio Code.

### Requirements
* Python 3.10+
* nvidia drivers if using a GPU for image processing (highly recommended)

### Setup
The fastest way to get started is using VS Code and [uv](https://astral.sh/uv):
```sh
uv sync
```

To download the paper dataset and extract it to the default location:
```sh
wget -nc -O "Microscope images.zip" "https://zenodo.org/records/13837238/files/Microscope%20images.zip?download=1"
unzip "Microscope images.zip"
```

Visual Studio Code will detect the creation of a new virtual environment in `.venv` and suggest to use it.

An alternative is using a dev container. Simply open the folder in Visual Studio Code (locally or on a remote machine) and select "Reopen in Container" from the notification that appears. This will build the dev container and open the folder in a new window. All dependencies will be installed automatically and supporting data downloaded and extracted from Zenodo.

[10.36227/techrxiv.173896967.76043093/v1]: https://doi.org/10.36227/techrxiv.173896967.76043093/v1