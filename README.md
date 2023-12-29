# Backtest-Frame-for-Machine-Learning-Alpha-Factors
Backtest Frame for Machine Learning Alpha Factors

## Introduction
Vision Transformers (ViTs) architecture have demonstrated promising performance in the field of computer vision. We are interested in implementing one of the popular ViTs - MViTv2 on one of the important computer vision tasks - Instance Segmentation. The PointRend method was developed to output high-quality instance segmentation. We implement the vision transformer based Mask R-CNNs with the PointRend method and evaluate its performance. We believe that the transformer architecture could potentially help extract more contextual and semantic information for the feature source in this case. Therefore, we implement the vision transformer based Mask R-CNN as well as using the PointRend method for our instance segmentation task. 

## Goals
- Implementing GANs from scratch using Pytorch.
- Understand the implementation of the original Mask R-CNN model, MViTv2 and PointRend method.
- Understand how above are implemented in Detectron2 framework.
- Implement Mask R-CNN using PyTorch from scratch.
- Update the CNN backbone of the Mask R-CNN with the Vision Transformer - MViTv2.
- Integrate the PointRend method to the transformer based Mask R-CNN model.
- Train the model using the COCO dataset (with downsized data + data augmentation).
- Evaluate the model.
- Train the network with the MNIST dataset to generate digit images.
- Improve the GANs with Deep Convolutional GANs and train it with custom dataset downloaded from Kaggle.
- Apply some variations such as using Spectral Normalization technique for training.

## Requirement
Packages required for this program is listed below:
- [Numpy](https://github.com/numpy): A package for numerical and matrix computation
- [Pandas](https://github.com/pandas): A package for dataframe processing
- [Matplotlib](https://github.com/matplotlib): A package for data manipulation and data plot
- [OpenCV](https://github.com/opencv/opencv): A package used for image and video processing
- [Pytorch](https://github.com/pytorch): A package used for image and video processing

## Code files:
- Generative_Adversarial_Network_V1.ipynb: Notebook Version 1
- Generative_Adversarial_Network_V1.py: Python Code Version 1
- Generative_Adversarial_Network_V2.ipynb: Notebook Version 2
- Generative_Adversarial_Network_V2.py: Python Code Version 2
- DCGAN_MNIST.ipynb：Generate MNIST digit images with Deep Convolutional GAN (DCGAN)
- DCGAN_MNIST.py: Generate MNIST digit images with Deep Convolutional GAN (DCGAN)
- DCGAN_CIFAR_no_Spectral Normalization.ipynb: Generate CIFAR-10 images with DCGAN
- DCGAN_CIFAR_no_Spectral Normalization.py: Generate CIFAR-10 images with DCGAN
- DCGAN_CIFAR_with_Spectral_Normalization.ipynb: Generate CIFAR-10 images with SN-DCGAN
- DCGAN_CIFAR_with_Spectral_Normalization.py: Generate CIFAR-10 images with SN-DCGAN

## Output Image files:
- Output_Images_V1: Generated Images x 100
- Research Paper
- Image Generation with SN-DCGAN on MNIST (Figure01)
- Image Generation with SN-DCGAN on CIFAR-10 (Figure02)

## Results:
- Image Generation with SN-DCGAN on MNIST: 
<img src="" width="600" height="300">
- Image Generation with SN-DCGAN on CIFAR-10:
<img src="" width="600" height="300">
