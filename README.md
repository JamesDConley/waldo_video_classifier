# Waldo Video Classifier

## 1. Purpose
This code is designed to simplify the training of deep learning models for classification of videos, specifically for detecting hackers in video games.

## 2. Usage
Currently, code is implemented only in notebooks

### 2.1 Docker
Note that GPU passthrough is not supported on windows- and generally I only test any of this in linux (specifically ubuntu) although it should be easy to adapt to other operating systems.

You can easily setup all dependencies if you have docker installed with the included `build_and_run.sh` script

```
cd docker
bash build_and_run.sh
```
This will drop you inside a docker container that has mounted the root directory of this repo.
You can then run the `start_jlab.sh` script in order to start jupyter lab and open the notebooks

```
bash start_jlab.sh
```
This will start a jupyter lab server, copy the link displayed in the CLI (including the token!) to access it

## Code Location
Proper code is under the `src` directory.

WIP code, and various experiments/examples are under the `notebooks` folder