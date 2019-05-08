# GPU-Setup for Ubuntu 16.04

Provide some script for cuda-cudnn set up. Forked from [this](https://github.com/AndyYSWoo/Azure-GPU-Setup).

We provide scripts to generate cuda-cudnn script.
Somehow, you need to download *Code Samples and User Guide* from nvidia's [download site](https://developer.nvidia.com/rdp/cudnn-download) and put it in this folder, registration needed.
#### Usage:
- Generate Scripts with assigned version
```
python3 gen_sh.py --cuda 9.0 --cudnn 7.4 --ubuntu 1604
```
- Install CUDA

```
sudo chmod +x gpu-setup-part1-cuda.sh
./gpu-setup-part1-cuda.sh
```
It will reboot the machine once process completed. Have a drink, this may take *20~30 min*, upto download time
- Install CUDNN
```
sudo chmod +x gpu-setup-part2-cudnn.sh
./gpu-setup-part2-cudnn.sh
```
This may take *~5 min*
- Have a tensorflow test
```
python3 gpu-test.py
```

#### Footnotes:
- We use cuda 9.0 and cudnn 7.4 as basic example here. For the further combination,  information can be find [cudnn version](https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1604/x86_64/), [cuda version](http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/). Or there ubuntu1804 version.


- We currently only support the following cudnn-cuda pair:
<p align="center">

|CUDNN| CUDA|
|:-----:|-----:|
|7.0  | 9.0|
|7.2  | 9.0|
|7.2  | 9.2|
|7.4  | 9.0|
|7.4  | 9.2|
|7.4  | 10.1|
|7.5  | 9.0|
|7.5  | 9.2|
|7.5  | 10.1|

- Multiple CUDA environment
These [site1](https://www.pugetsystems.com/print_pdf.php?url=https://www.pugetsystems.com/labs/hpc/How-To-Install-CUDA-10-together-with-9-2-on-Ubuntu-18-04-with-support-for-NVIDIA-20XX-Turing-GPUs-1236/&loaded=1), [site2](https://blog.kovalevskyi.com/multiple-version-of-cuda-libraries-on-the-same-machine-b9502d50ae77) may helpful.
