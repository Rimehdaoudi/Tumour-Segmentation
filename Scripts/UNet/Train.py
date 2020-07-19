import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

import cv2
import numpy as np
from glob import glob
import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

from tensorflow.keras.layers import Conv2D, Activation, BatchNormalization
from tensorflow.keras.layers import UpSampling2D, Input, Concatenate, MaxPool2D
from tensorflow.keras.models import Model
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint, ReduceLROnPlateau, CSVLogger, TensorBoard
from tensorflow.keras.metrics import Recall, Precision
from keras.utils import CustomObjectScope
from Data import load_data, tf_dataset
from Model import build_model

def iou(y_true, y_pred):
    def f(y_true, y_pred):
        intersection = (y_true * y_pred).sum()
        union = y_true.sum() + y_pred.sum() - intersection
        x = (intersection + 1e-15) / (union + 1e-15)
        x = x.astype(np.float32)
        return x
    return tf.numpy_function(f, [y_true, y_pred], tf.float32)

if __name__ == "__main__":
    PATH = "../Dataset/UNET-Data/"
    (train_x, train_y), (valid_x, valid_y), (test_x, test_y) = load_data(PATH)

    BATCH = 8
    lr = 1e-4
    epochs = 50

    train_dataset = tf_dataset(train_x, train_y, batch=BATCH)
    valid_dataset = tf_dataset(valid_x, valid_y, batch=BATCH)

    model = build_model()
    opt = tf.keras.optimizers.Adam(lr)
    metrics = ["acc", Recall(), Precision(), iou]
    model.compile(loss="binary_crossentropy", optimizer=opt, metrics=metrics)

    callbacks = [
    	ModelCheckpoint("model.h5"),
    	ReduceLROnPlateau(monitor="val_loss", factor=0.1, patience=3),
    	CSVLogger("data.csv"),
    	TensorBoard(),
    	EarlyStopping(monitor="val_loss", patience=10, restore_best_weights=False)
    ]

    train_steps = len(train_x) // BATCH
    valid_steps = len(valid_x) // BATCH

    if len(train_x) % BATCH != 0:
        train_steps += 1
    if len(valid_x) % BATCH != 0:
        valid_steps += 1

    model.fit(
        train_dataset,
        validation_data=valid_dataset,
        epochs=epochs,
        steps_per_epoch=train_steps,
        validation_steps=valid_steps,
        callbacks=callbacks
    )
