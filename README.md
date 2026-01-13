## Fourier-KAN: Feature Distribution Decomposition and Recombination for Unknown-Domain Object Detection

### 🚀 Overview / 项目简介

This repository contains the official implementation of **["Fourier-KAN: Feature Distribution Decomposition and Recombination for Unknown-Domain Object Detection"]**.

  ![Image text](https://github.com/2490o/Fourier-KAN/blob/main/figures/f2.png)

## Installation 

`conda` virtual environment is recommended.

```
conda create -n Fourier-KAN python=3.9
conda activate Fourier-KAN
pip install -r requirements.txt
pip install -e .
```

## Training

```
CUDA_VISIBLE_DEVICES=1 python train.py
```

## Validation

```
CUDA_VISIBLE_DEVICES=1 python train.py
```

### Dataset Release (VOC & YOLO)

We provide the dataset in **two formats** for convenience: **Pascal VOC (XML)** and **YOLO (TXT)**.

- **VOC (domain.zip)**  
  Link: https://pan.baidu.com/s/1m134GQdnJ7wmhu7KLMXERg  
  Code (提取码): `e8kf`

- **YOLO (YOLOdata.zip)**  
  Link: https://pan.baidu.com/s/1nsS25a7JBDkexjsG2Rvf0A  
  Code (提取码): `7tk5`