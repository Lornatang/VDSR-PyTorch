# VDSR-PyTorch

### Overview

This repository contains an op-for-op PyTorch reimplementation of [Accurate Image Super-Resolution Using Very Deep Convolutional Networks](https://arxiv.org/abs/1511.04587).

### Table of contents

- [VDSR-PyTorch](#vdsr-pytorch)
    - [Overview](#overview)
    - [Table of contents](#table-of-contents)
    - [About Accurate Image Super-Resolution Using Very Deep Convolutional Networks](#about-accelerating-the-super-resolution-convolutional-neural-network)
    - [Download weights](#download-weights)
    - [Download datasets](#download-datasets)
        - [Download train dataset](#download-train-dataset)
        - [Download valid dataset](#download-valid-dataset)
    - [Test](#test)
    - [Train](#train)
    - [Result](#result)
    - [Credit](#credit)
        - [Accelerating the Super-Resolution Convolutional Neural Network](#accurate-image-super-resolution-using-very-deep-convolutional-networks)

## About Accelerating the Super-Resolution Convolutional Neural Network

If you're new to VDSR, here's an abstract straight from the paper:

We present a highly accurate single-image superresolution (SR) method. Our method uses a very deep convolutional network inspired by VGG-net used for
ImageNet classification. We find increasing our network depth shows a significant improvement in accuracy. Our finalmodel uses 20 weight layers. By
cascading small filters many times in a deep network structure, contextual information over large image regions is exploited in an efficient way. With
very deep networks, however, convergence speed becomes a critical issue during training. We propose a simple yet effective training procedure. We
learn residuals onlyb and use extremely high learning rates
(104 times higher than SRCNN) enabled by adjustable gradient clipping. Our proposed method performs better than existing methods in accuracy and
visual improvements in our results are easily noticeable.

## Download weights

- [Google Driver](https://drive.google.com/drive/folders/1vrf4VdjuQXCmVo0uqs3kTlls-fPaRRpc?usp=sharing)
- [Baidu Driver](https://pan.baidu.com/s/16HnByHXp0cW57RfpdwHahQ) access:`llot`

## Download datasets

### Download train dataset

#### TB291

- Image format
    - [Google Driver](https://drive.google.com/drive/folders/13wiE6YqIhyix0RFxpFONJ7Zz_00CttdX?usp=sharing)
    - [Baidu Driver](https://pan.baidu.com/s/1mhbFj0Nvwthmgx07Gas5BQ) access: `llot`

- LMDB format (train)
    - [Google Driver](https://drive.google.com/drive/folders/1BPqN08QHk_xFnMJWMS8grfh_vesVs8Jf?usp=sharing)
    - [Baidu Driver](https://pan.baidu.com/s/1eqeORnKcTmGatx2kAG92-A) access: `llot`

- LMDB format (valid)
    - [Google Driver](https://drive.google.com/drive/folders/1bYqqKk6NJ9wUfxTH2t_LbdMTB04OUicc?usp=sharing)
    - [Baidu Driver](https://pan.baidu.com/s/1W34MeEtLY0m-bOrnaveVmw) access: `llot`

### Download valid dataset

#### Set5

- Image format
    - [Google Driver](https://drive.google.com/file/d/1GtQuoEN78q3AIP8vkh-17X90thYp_FfU/view?usp=sharing)
    - [Baidu Driver](https://pan.baidu.com/s/1dlPcpwRPUBOnxlfW5--S5g) access:`llot`

#### Set14

- Image format
    - [Google Driver](https://drive.google.com/file/d/1CzwwAtLSW9sog3acXj8s7Hg3S7kr2HiZ/view?usp=sharing)
    - [Baidu Driver](https://pan.baidu.com/s/1KBS38UAjM7bJ_e6a54eHaA) access:`llot`

#### BSD200

- Image format
    - [Google Driver](https://drive.google.com/file/d/1cdMYTPr77RdOgyAvJPMQqaJHWrD5ma5n/view?usp=sharing)
    - [Baidu Driver](https://pan.baidu.com/s/1xahPw4dNNc3XspMMOuw1Bw) access:`llot`

## Test

Modify the contents of the file as follows.

- line 24: `upscale_factor` change to the magnification you need to enlarge.
- line 25: `mode` change Set to valid mode.
- line 84: `model_path` change weight address after training.

## Train

Modify the contents of the file as follows.

- line 24: `upscale_factor` change to the magnification you need to enlarge.
- line 25: `mode` change Set to train mode.

If you want to load weights that you've trained before, modify the contents of the file as follows.

- line 56: `resume` change to `True`.
- line 57: `strict` Transfer learning is set to `False`, incremental learning is set to `True`.
- line 58: `start_epoch` change number of training iterations in the previous round.
- line 59: `resume_weight` the weight address that needs to be loaded.

## Result

Source of original paper results: https://arxiv.org/pdf/1511.04587.pdf

In the following table, the value in `()` indicates the result of the project, and `-` indicates no test.

| Dataset | Scale |       PSNR       |
| :-----: | :---: | :--------------: |
|  Set5   |   2   | 37.53(**37.44**) |
|  Set5   |   3   | 33.66(**33.69**) |
|  Set5   |   4   | 31.35(**31.28**) |

Low Resolution / Super Resolution / High Resolution
<span align="center"><img src="assets/result.png"/></span>

### Credit

#### Accurate Image Super-Resolution Using Very Deep Convolutional Networks

_Jiwon Kim, Jung Kwon Lee, Kyoung Mu Lee_ <br>

**Abstract** <br>
We present a highly accurate single-image superresolution (SR) method. Our method uses a very deep convolutional network inspired by VGG-net used for
ImageNet classification. We find increasing our network depth shows a significant improvement in accuracy. Our finalmodel uses 20 weight layers. By
cascading small filters many times in a deep network structure, contextual information over large image regions is exploited in an efficient way. With
very deep networks, however, convergence speed becomes a critical issue during training. We propose a simple yet effective training procedure. We
learn residuals onlyb and use extremely high learning rates
(104 times higher than SRCNN) enabled by adjustable gradient clipping. Our proposed method performs better than existing methods in accuracy and
visual improvements in our results are easily noticeable.

[[Paper]](https://arxiv.org/pdf/1511.04587)

```
@inproceedings{vedaldi15matconvnet,
  author    = {A. Vedaldi and K. Lenc},
  title     = {MatConvNet -- Convolutional Neural Networks for MATLAB},
  booktitle = {Proceeding of the {ACM} Int. Conf. on Multimedia},
  year      = {2015},
}
```
