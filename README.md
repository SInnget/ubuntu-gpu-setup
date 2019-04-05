# GPU-Setup for Ubuntu 16.04

Provide some script for cuda-cudnn set up. Forked from [this](https://github.com/AndyYSWoo/Azure-GPU-Setup).

We provide scripts to generate cuda-cudnn script.

#### Usage:
- Generate Scripts with assigned version
```
python3 gen_sh.py --cuda 9.0 --cudnn 7.4
```
- Install CUDA


```
sudo chmod +x gpu-setup-part1-cuda.sh
./gpu-setup-part1-cuda.sh
```
- Install CUDNN
```
sudo chmod +x gpu-setup-part2-cudnn.sh
./gpu-setup-part2-cudnn.sh
```

#### Footnotes:
We use cuda 9.0 and cudnn 7.4 as basic example here. For the further combination,  information can be find [cudnn version](https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1604/x86_64/), [cuda version](http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/).


We currently only support the following cudnn-cuda pair:

|CUDNN| CUDA|
|:-----:|-----:|
|7.0  | 9.0|
|7.2  | 9.0|
|7.2  | 9.2|
|7.4  | 9.0|
|7.4  | 9.2|
|7.4  | 10.0|
|7.5  | 9.0|
|7.5  | 9.2|
|7.5  | 10.0|