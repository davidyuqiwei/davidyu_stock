#from tensorflow import keras
from sklearn import metrics
from keras.models import Sequential
from keras.layers import Conv1D,MaxPooling1D,Dropout,Flatten,BatchNormalization,Dense,Embedding,Activation
import numpy as np
import keras
from keras.optimizers import SGD
#x_train = np.expand_dims(np.random.normal(size=(3881, 10)),axis=-1)
#y_train = np.random.choice([0,1], size=(3881,1))


"""
def CNN_model(x_train, y_train,n_features,x_test,y_test):
    model = Sequential()
    model.add(Conv1D(filters=30, kernel_size=1,activation='relu',input_shape=( n_features,1 )))
    model.add(Dropout(0.1))
    model.add(Conv1D(filters=20, kernel_size=1, activation='relu'))
    model.add(Dropout(0.1))
    model.add(MaxPooling1D(pool_size=2))
    model.add(Flatten())
    model.add(Dense(20, activation='relu'))
    model.add(Dropout(0.1))
    model.add(Dense(3, activation='softmax'))
    sgd = SGD(lr=0.1, decay=1e-6, momentum=0.9, nesterov=True)
    model.compile(loss='categorical_crossentropy',optimizer=sgd,metrics=['accuracy'])
    one_hot_labels = keras.utils.to_categorical(y_train,num_classes=3)
    model.fit(x_train,one_hot_labels,epochs=15, batch_size=200)
    return model

"""

def CNN_model(x_train,y_train):
    model = Sequential()
    model.add(Conv1D(256, 5, padding='same'))
    model.add(MaxPooling1D(3, 3, padding='same'))
    model.add(Conv1D(128, 5, padding='same'))
    model.add(MaxPooling1D(3, 3, padding='same'))
    model.add(Conv1D(64, 3, padding='same'))
    model.add(Flatten())
    model.add(Dropout(0.1))
    model.add(BatchNormalization())  # (批)规范化层
    model.add(Dense(256, activation='relu'))
    model.add(Dropout(0.1))
    model.add(Dense(3, activation='softmax'))
    sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
    model.compile(loss='categorical_crossentropy',optimizer=sgd,metrics=['accuracy'])
    one_hot_labels = keras.utils.to_categorical(y_train, num_classes=3)  # 将标签转换为one-hot编码
    model.fit(x_train, one_hot_labels,epochs=50, batch_size=300)
    return model


"""
def CNN_model(x_train, y_train,n_features):
    model = Sequential() #建立模型
    model.add(Dense(input_dim = 120, output_dim = 240)) #添加输入层、隐藏层的连接
    model.add(Activation('relu')) #以Relu函数为激活函数
    model.add(Dense(input_dim = 240, output_dim = 120)) #添加隐藏层、隐藏层的连接
    model.add(Activation('relu')) #以Relu函数为激活函数
    model.add(Dense(input_dim = 120, output_dim = 120)) #添加隐藏层、隐藏层的连接
    model.add(Activation('relu')) #以Relu函数为激活函数
    model.add(Dense(input_dim = 120, output_dim = 20)) #添加隐藏层、输出层的连接
    model.add(Activation('sigmoid')) #以sigmoid函数为激活函数
    #编译模型，损失函数为binary_crossentropy，用adam法求解
    model.compile(loss='mean_squared_error', optimizer='adam')
    
    model.fit(x_train, y_train, nb_epoch = 100, batch_size = 8) #训练模型
    return model

"""
