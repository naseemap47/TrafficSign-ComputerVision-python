# TrafficSign-ComputerVision-python

<p align="center">
 <a href="https://github.com/naseemap47/TrafficSign-ComputerVision-python">
    <img alt="Python3" src="https://img.shields.io/badge/Language-Python3-yellowgreen?color=brightgreen&logo=python">
  </a>
  <a href="https://github.com/naseemap47/TrafficSign-ComputerVision-python/issues">
    <img alt="Top-down learning path: TrafficSign-ComputerVision-python" src="https://img.shields.io/github/issues/naseemap47/TrafficSign-ComputerVision-python?color=9cf&style=flat&logo=appveyor">
  </a>
  <a href="https://github.com/naseemap47/TrafficSign-ComputerVision-python/stargazers">
    <img alt="GitHub stars" src="https://img.shields.io/github/stars/naseemap47/TrafficSign-ComputerVision-python?color=success&style=flat&logo=appveyor">
  </a>
  <a href="https://github.com/naseemap47/TrafficSign-ComputerVision-python/network">
    <img alt="GitHub forks" src="https://img.shields.io/github/forks/naseemap47/TrafficSign-ComputerVision-python?style=flat&logo=Git">
  </a>
  <a href="https://github.com/naseemap47/TrafficSign-ComputerVision-python/blob/master/LICENSE">
    <img alt="GitHub Licence" src="https://img.shields.io/github/license/naseemap47/TrafficSign-ComputerVision-python?color=red&style=flat&logo=appveyor">
  </a>
  <a href="https://www.linkedin.com/in/naseem-alassampattil/">
    <img alt="Linkedin" src="https://img.shields.io/badge/Linkedin-blue?logo=linkedin">
  </a>
 <a href="https://github.com/naseemap47">
    <img alt="Github" src="https://img.shields.io/badge/Github-black?logo=github">
 </a>
 <a href="https://github.com/naseemap47/TrafficSign-ComputerVision-python">
    <img alt="VS Code" src="https://img.shields.io/badge/IDE-VS Code-yellowgreen?color=brightgreen&logo=visualstudiocode">
  </a>
</p>

## Description
Predict traffic sign boards using Deep-Learning Model (Tensorflow)

## ⚠️ Limitations
* Due to my system limitaion I can't create very deep nerural networks
* I can only taken batch_size = 32 (system limitaions)
* Only trained neural networks by 2 epochs (system limitaions)

## 💡 Suggestions
* Increase depth of nreural networks
* Increase batch_size
* Increase number of epochs
* Experiment with preprocessor

## Requirements
#### Programming Language
* Python3 (VS Code)
#### Libraries
##### Data Cleaning
* os
* glob
* shutil
* csv
* sklearn (train-val split)
##### Data Manipulation
* Numpy
* Pandas
##### DeepLearning Model
* Tensorflow
* Keras

## Project Structure
* Data Cleaning
#### DeepLearning Model
* Sequential Layers
* Created generators
* Fitted model using **Train Data**
* Saved DeepLearning Model in **h5** file format
* Load saved Model
* Evalute Test data using using saved Model
* predict Traffic-Sign boards using Model

## Project Setup
* Clone project
* Create a branch
* Make changes in Sequential Layers and preprocessor to reduce validation loss
* Fit model by using Train Data
* Save Model in h5 format
* Create a pull request

## License
[![CC0](http://seawisphunter.com/minibuffer/api/MIT-License-transparent.png)](https://github.com/naseemap47/TrafficSign-ComputerVision-python/blob/master/LICENSE)
