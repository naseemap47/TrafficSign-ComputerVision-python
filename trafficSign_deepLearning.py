from my_utils import create_generators
from deepLearning_model import trafficSign_model

if __name__=='__main__':

    path_to_train = '/home/naseem/My Project/TrafficSign-ComputerVision-python/training_data/train'
    path_to_val = '/home/naseem/My Project/TrafficSign-ComputerVision-python/training_data/val'
    path_to_test = '/home/naseem/My Project/TrafficSign-ComputerVision-python/test'

    train_generators, val_generators, test_generators = create_generators(
        batch_size=32,
        path_to_train_data=path_to_train,
        path_to_val_data=path_to_val,
        path_to_test_data=path_to_test
    )
    number_classes = train_generators.num_classes

    model = trafficSign_model(no_classes=number_classes)
    model.compile(
        optimizer='adam',
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )
    model.fit(
        train_generators,
        batch_size=32,
        epochs=2,
        validation_data=val_generators,
    )