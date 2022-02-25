import os
import glob
import shutil
from sklearn.model_selection import train_test_split
import shutil
import csv
from tensorflow.keras.preprocessing.image import ImageDataGenerator

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

                
def create_generators(batch_size, path_to_train_data, path_to_val_data, path_to_test_data):
    preprocessor = ImageDataGenerator(
        rescale = 1/225,
        rotation_range=10,
        width_shift_range=0.1,
        height_shift_range=0.1
    )
    test_preprocessor = ImageDataGenerator(
        rescale = 1 / 225
    )
    train_generators = preprocessor.flow_from_directory(
        path_to_train_data,
        target_size=(70,70),
        color_mode='rgb',
        class_mode='categorical',
        batch_size=batch_size,
        shuffle=True
    )
    val_generators = test_preprocessor.flow_from_directory(
        path_to_val_data,
        target_size=(70,70),
        color_mode='rgb',
        class_mode='categorical',
        batch_size=batch_size,
        shuffle=False
    )
    test_generators = test_preprocessor.flow_from_directory(
        path_to_test_data,
        target_size=(70,70),
        color_mode='rgb',
        class_mode='categorical',
        batch_size=batch_size,
        shuffle=False
    )
    return train_generators, val_generators, test_generators

