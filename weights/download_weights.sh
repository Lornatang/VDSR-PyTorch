#!/bin/bash

echo "Start downloading pre training model..."
wget https://github.com/Lornatang/VDSR-PyTorch/releases/download/1.0/vdsr_2x.pth
wget https://github.com/Lornatang/VDSR-PyTorch/releases/download/1.0/vdsr_3x.pth
wget https://github.com/Lornatang/VDSR-PyTorch/releases/download/1.0/vdsr_4x.pth
echo "All pre training models have been downloaded!"
