from my_utils import create_generators
from deepLearning_model import trafficSign_model
from tensorflow.keras.callbacks import EarlyStopping
import os
from tensorflow.keras.models import load_model
from my_utils import predict_with_model

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

    # swiches
    TRAIN = False
    TEST = False
    PREDICT = True

    if TRAIN:
        number_classes = train_generators.num_classes
        early_stopping = EarlyStopping(
            min_delta=0.001,
            patience=10,
            mode='min',
            restore_best_weights=True,
            verbose=1
        )

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
            callbacks=[early_stopping]
        )

        # Save Model in a h5 format
    
        if os.path.isfile(
        '/home/naseem/My Project/TrafficSign-ComputerVision-python//Model.h5'
        ) is False:
            model.save(
                '/home/naseem/My Project/TrafficSign-ComputerVision-python//Model.h5'
            )

    if TEST:
        saved_model = load_model('/home/naseem/My Project/TrafficSign-ComputerVision-python//Model.h5')
        saved_model.summary()

        # Evaluate Validation dataset
        print("Evaluate Validation data:")
        saved_model.evaluate(val_generators)

        # Evaluate Test dataset
        print("Evaluate Test data:")
        saved_model.evaluate(test_generators)

    if PREDICT:
        img_path = '/home/naseem/My Project/TrafficSign-ComputerVision-python/train/17/00017_00000_00018.png'
        model = load_model('/home/naseem/My Project/TrafficSign-ComputerVision-python//Model.h5')


        prediction = predict_with_model(img_path=img_path, model=model)

        print("Prediction:", prediction)
