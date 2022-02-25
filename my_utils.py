import os
import glob
import shutil
from sklearn.model_selection import train_test_split
import shutil
import csv

def split_data(path_to_data, path_to_save_train, path_to_save_val, split_size=0.2):
    
    folders = os.listdir(path_to_data)

    for folder in folders:

        full_path = os.path.join(path_to_data, folder)
        path_to_images = glob.glob(os.path.join(full_path, '*png'))

        x_train, x_val = train_test_split(path_to_images, test_size=split_size)

        for x in x_train:
            path_to_folder = os.path.join(path_to_save_train, folder)

            if not os.path.isdir(path_to_folder):
                os.makedirs(path_to_folder)

            shutil.copy(x, path_to_folder)

        for x in x_val:
            path_to_folder = os.path.join(path_to_save_val, folder)

            if not os.path.isdir(path_to_folder):
                os.makedirs(path_to_folder)

            shutil.copy(x, path_to_folder)

def order_test_data(path_to_csv, path_to_data):
    try:
        with open(path_to_csv, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
        
            for i,row in enumerate(reader):
                if i==0:
                    continue

                img_name = row[-1].replace('Test/', '')
                label = row[-2]

                path_to_folder = os.path.join(path_to_data, label)
                img_full_path = os.path.join(path_to_data, img_name)

                if not os.path.isdir(path_to_folder):
                    os.makedirs(path_to_folder)

                shutil.move(img_full_path, path_to_folder)
    except:
        print("[INFO] : Error reading csv file")

                


