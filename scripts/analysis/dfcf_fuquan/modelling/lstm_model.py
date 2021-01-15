# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from keras.layers import Dropout,LSTM,Dense
from keras.models import Sequential
import numpy as np
from keras import optimizers


class DL_model:
    def __init__(self,X_train, X_test, y_train, y_test, **kwargs):
        self.X_train = X_train
        self.X_test = X_test
        self.y_train = y_train
        self.y_test = y_test
        self.model = ''


    def load_model2(x_train,y_train):
        x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
        y_train = np.reshape(y_train,(y_train.shape[0], 1))
        #x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
        model = Sequential()
        model.add(LSTM(20, input_shape=(x_train.shape[1], x_train.shape[2]),return_sequences=True))
        model.add(Dropout(0.1))
        model.add(LSTM(20,input_shape=(x_train.shape[1], x_train.shape[2]),return_sequences=False))
        model.add(Dropout(0.1))
        #model.add(Dense(y_train.shape[1]))
        model.add(Dense(1))
    
        sgd = optimizers.SGD(lr=0.02, decay=1e-6, momentum=0.9, nesterov=True)
        model.compile(loss='binary_crossentropy', optimizer=sgd,metrics=['accuracy'])
        return model

    def load_model3(self):
        """
        LSTM
        """
        self.X_train = np.reshape(self.X_train, (self.X_train.shape[0], self.X_train.shape[1], 1))
        self.X_test = np.reshape(self.X_test, (self.X_test.shape[0], self.X_test.shape[1], 1))
        self.y_train = np.reshape(self.y_train,(self.y_train.shape[0], 1))
        #x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
        model = Sequential()
        model.add(LSTM(20,activation='relu', input_shape=(self.X_train.shape[1], self.X_train.shape[2]),return_sequences=True))
        model.add(Dropout(0.1))
        model.add(LSTM(20,activation='relu',input_shape=(self.X_train.shape[1], self.X_train.shape[2]),return_sequences=False))
        model.add(Dropout(0.2))
        #model.add(Dense(y_train.shape[1]))
        model.add(Dense(1,activation='sigmoid'))
    
        sgd = optimizers.SGD(lr=0.05, decay=1e-6, momentum=0.9, nesterov=True)
        model.compile(loss='binary_crossentropy', optimizer=sgd,metrics=['accuracy'])
        self.model = model
        return self

    def load_model4(self):
        #x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
        #self.X_train = np.reshape(self.X_train, (self.X_train.shape[0], self.X_train.shape[1], 1))
        #y_train = np.reshape(y_train,(y_train.shape[0], 1))
        #x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
        model = Sequential()
        model.add(Conv2D(170, 1,4,activation='relu', input_shape=(self.X_train.shape[1], )))
        model.add(Dense(16,activation='relu'))
        model.add(Dense(8,activation='relu'))
        model.add(Dense(4,activation='relu'))
        model.add(Dense(1,activation='sigmoid'))
        sgd = optimizers.SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
        model.compile(loss='binary_crossentropy', optimizer=sgd,metrics=['accuracy'])
        self.model = model
        return self


