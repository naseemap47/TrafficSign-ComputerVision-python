import os
import glob
import shutil
from sklearn.model_selection import train_test_split
import shutil
from my_utils import split_data


if __name__=='__main__':

    path_to_data = '/home/naseem/My Project/TrafficSign-ComputerVision-python/train'
    path_to_save_train = '/home/naseem/My Project/TrafficSign-ComputerVision-python/training_data/train'
    path_to_save_val = '/home/naseem/My Project/TrafficSign-ComputerVision-python/training_data/val'

    split_data(path_to_data, path_to_save_train, path_to_save_val)
