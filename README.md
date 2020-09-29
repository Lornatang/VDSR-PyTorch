# VDSR-PyTorch

### Overview
This repository contains an op-for-op PyTorch reimplementation of 
[Accurate Image Super-Resolution Using Very Deep Convolutional Networks](https://arxiv.org/abs/1511.04587).

### Table of contents
1. [Accurate Image Super-Resolution Using Very Deep Convolutional Networks](#about-accurate-image-super-resolution-using-very-deep-convolutional-networks)
2. [Installation](#installation)
    * [Clone and install requirements](#clone-and-install-requirements)
    * [Download pretrained weights](#download-pretrained-weights)
    * [Download dataset](#download-dataset)
3. [Test](#test)
4. [Train](#train-eg-voc2012)
    * [Example](#example-eg-voc2012)
5. [Contributing](#contributing) 
6. [Credit](#credit)

### About Accurate Image Super-Resolution Using Very Deep Convolutional Networks

If you're new to VDSR, here's an abstract straight from the paper:

We present a highly accurate single-image superresolution (SR) method. 
Our method uses a very deep convolutional network inspired by VGG-net used for ImageNet classification. 
We find increasing our network depth shows a significant improvement in accuracy. 
Our finalmodel uses 20 weight layers. By cascading small filters many times in a deep network structure, 
contextual information over large image regions is exploited in an efficient way. 
With very deep networks, however, convergence speed becomes a critical issue during training. 
We propose a simple yet effective training procedure. We learn residuals onlyb and use extremely high learning rates 
(104 times higher than SRCNN) enabled by adjustable gradient clipping.
Our proposed method performs better than existing methods in accuracy and visual improvements in our results are
easily noticeable.

### Installation

#### Clone and install requirements

```bash
git clone https://github.com/Lornatang/VDSR-PyTorch.git
cd VDSR-PyTorch/
pip install -r requirements.txt
```

#### Download pretrained weights

```bash
cd weights/
bash download_weights.sh
```

#### Download dataset

```bash
cd data/
bash download_dataset.sh
```

### Test

Evaluate the overall performance of the network.
```bash
usage: test.py [-h] [--dataroot DATAROOT] [--scale-factor {2,3,4}]
               [--weights WEIGHTS] [--cuda]

Accurate Image Super-Resolution Using Very Deep Convolutional Networks

optional arguments:
  -h, --help            show this help message and exit
  --dataroot DATAROOT   The directory address where the image needs to be
                        processed. (default: `./data/Set5`).
  --scale-factor {2,3,4}
                        Image scaling ratio. (default: 4).
  --weights WEIGHTS     Generator model name. (default:`weights/vdsr_4x.pth`)
  --cuda                Enables cuda

# Example
python test.py --dataroot ./data/Set5 --scale-factor 4 --weights ./weights/vdsr_4x.pth --cuda
```

Evaluate the benchmark of validation data set in the network
```bash
usage: test_benchmark.py [-h] [--dataroot DATAROOT] [-j N]
                         [--image-size IMAGE_SIZE] --scale-factor {2,3,4}
                         --weights WEIGHTS [--cuda]

Accurate Image Super-Resolution Using Very Deep Convolutional Networks

optional arguments:
  -h, --help            show this help message and exit
  --dataroot DATAROOT   Path to datasets. (default:`./data/VOC2012`)
  -j N, --workers N     Number of data loading workers. (default:4)
  --image-size IMAGE_SIZE
                        Size of the data crop (squared assumed). (default:256)
  --scale-factor {2,3,4}
                        Low to high resolution scaling factor.
  --weights WEIGHTS     Path to weights.
  --cuda                Enables cuda

# Example
python test_benchmark.py --dataroot ./data/VOC2012 --scale-factor 4 --weights ./weights/vdsr_4x.pth --cuda
```

Test single picture
```bash
usage: test_image.py [-h] [--file FILE] [--scale-factor {2,3,4}]
                     [--weights WEIGHTS] [--cuda]

Accurate Image Super-Resolution Using Very Deep Convolutional Networks

optional arguments:
  -h, --help            show this help message and exit
  --file FILE           Test low resolution image name.
                        (default:`./assets/baby.png`)
  --scale-factor {2,3,4}
                        Super resolution upscale factor. (default:4)
  --weights WEIGHTS     Generator model name. (default:`weights/vdsr_4x.pth`)
  --cuda                Enables cuda

# Example
python test_image.py --file ./assets/baby.png --scale-factor 4 ---weights ./weights/vdsr_4x.pth -cuda
```

Test single video
```bash
usage: test_video.py [-h] --file FILE --scale-factor {2,3,4} --weights WEIGHTS
                     [--view] [--cuda]

Accurate Image Super-Resolution Using Very Deep Convolutional Networks

optional arguments:
  -h, --help            show this help message and exit
  --file FILE           Test low resolution video name.
  --scale-factor {2,3,4}
                        Super resolution upscale factor. (default:4)
  --weights WEIGHTS     Generator model name.
  --view                Super resolution real time to show.
  --cuda                Enables cuda

# Example
python test_video.py --file ./data/1.mp4 --scale-factor 4 --weights ./weights/vdsr_4x.pth --view --cuda
```

Low resolution / Recovered High Resolution / Ground Truth

<span align="center"><img src="assets/result.png" alt="">
</span>

### Train (e.g VOC2012)

```bash
usage: train.py [-h] [--dataroot DATAROOT] [-j N] [--epochs N]
                [--image-size IMAGE_SIZE] [-b N] [--lr LR]
                [--momentum MOMENTUM] [--weight-decay WEIGHT_DECAY]
                [--clip CLIP] [--scale-factor {2,3,4}] [--weights WEIGHTS]
                [-p N] [--manualSeed MANUALSEED] [--cuda]

Accurate Image Super-Resolution Using Very Deep Convolutional Networks

optional arguments:
  -h, --help            show this help message and exit
  --dataroot DATAROOT   Path to datasets. (default:`./data/VOC2012`)
  -j N, --workers N     Number of data loading workers. (default:4)
  --epochs N            Number of total epochs to run. (default:100)
  --image-size IMAGE_SIZE
                        Size of the data crop (squared assumed). (default:256)
  -b N, --batch-size N  mini-batch size (default: 16), this is the total
                        batch size of all GPUs on the current node when using
                        Data Parallel or Distributed Data Parallel.
  --lr LR               Learning rate. (default:0.1)
  --momentum MOMENTUM   Momentum, (default:0.9)
  --weight-decay WEIGHT_DECAY
                        Weight decay. (default:0.0001).
  --clip CLIP           Clipping Gradients. (default:0.4).
  --scale-factor {2,3,4}
                        Low to high resolution scaling factor. (default:4).
  --weights WEIGHTS     Path to weights (to continue training).
  -p N, --print-freq N  Print frequency. (default:5)
  --manualSeed MANUALSEED
                        Seed for initializing training. (default:0)
  --cuda                Enables cuda
```

#### Example (e.g VOC2012)

```bash
python train.py --dataroot ./data/VOC2012 --scale-factor 4 --cuda
```

If you want to load weights that you've trained before, run the following command.

```bash
python train.py --dataroot ./data/VOC2012 --scale-factor 4 --weights ./weights/vdsr_4x_epoch_100.pth --cuda
```

### Contributing

If you find a bug, create a GitHub issue, or even better, submit a pull request. Similarly, if you have questions, simply post them as GitHub issues.   

I look forward to seeing what the community does with these models! 

### Credit

#### Accurate Image Super-Resolution Using Very Deep Convolutional Networks
_Jiwon Kim, Jung Kwon Lee, Kyoung Mu Lee_ <br>

**Abstract** <br>
We present a highly accurate single-image superresolution (SR) method. 
Our method uses a very deep convolutional network inspired by VGG-net used for ImageNet classification. 
We find increasing our network depth shows a significant improvement in accuracy. 
Our finalmodel uses 20 weight layers. By cascading small filters many times in a deep network structure, 
contextual information over large image regions is exploited in an efficient way. 
With very deep networks, however, convergence speed becomes a critical issue during training. 
We propose a simple yet effective training procedure. We learn residuals onlyb and use extremely high learning rates 
(104 times higher than SRCNN) enabled by adjustable gradient clipping.
Our proposed method performs better than existing methods in accuracy and visual improvements in our results are
easily noticeable.

[[Paper]](https://arxiv.org/pdf/1511.04587)

```
@inproceedings{vedaldi15matconvnet,
  author    = {A. Vedaldi and K. Lenc},
  title     = {MatConvNet -- Convolutional Neural Networks for MATLAB},
  booktitle = {Proceeding of the {ACM} Int. Conf. on Multimedia},
  year      = {2015},
}
```
