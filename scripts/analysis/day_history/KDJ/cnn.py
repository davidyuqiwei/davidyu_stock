import os
os.system("sh /usr/davidyu/tensorflow.sh")
from sklearn.model_selection import train_test_split
import pandas as pd
import jieba
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import keras
#from tensorflow import keras
from sklearn import metrics
from keras.models import Sequential
from keras.layers import Conv1D,MaxPooling1D,Dropout,Flatten,BatchNormalization,Dense,Embedding
import numpy as np

#x_train = np.expand_dims(np.random.normal(size=(3881, 10)),axis=-1)
#y_train = np.random.choice([0,1], size=(3881,1))



def CNN_model(x_train, y_train,n_features):
    model = Sequential()
    model.add(Conv1D(filters=100, kernel_size=1,activation='relu',input_shape=( n_features,1 )))
    model.add(Conv1D(filters=100, kernel_size=1, activation='relu'))
    model.add(Dropout(0.1))
    model.add(MaxPooling1D(pool_size=2))
    model.add(Flatten())
    model.add(Dense(100, activation='relu'))
    model.add(Dense(3, activation='softmax'))
    model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
    one_hot_labels = keras.utils.to_categorical(y_train,num_classes=3)
    model.fit(x_train,one_hot_labels,epochs=20, batch_size=32)
    return model


def load_data():
    file_name = "/home/davidyu/stock/data/test/SH_index_kdj_macd_rsi_test.csv"
    df1 = pd.read_csv(file_name)
    df1["slopes"][df1["slopes"]==-1]=0
    feature_list = ['kdjk','kdjd','kdjj','macdh','rsi_6','wr_6','wr_10','wr_20',
                    'rsi_12','rsi_24']
    Y = df1.slopes.values
    X = df1[feature_list].values
    return X,Y
X,Y = load_data()
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=.3)
x_train = np.expand_dims(x_train,axis=-1)
y_train = np.expand_dims(y_train,axis=-1)
n_timesteps, n_features, n_outputs =x_train.shape[0], x_train.shape[1], y_train.shape[1]


model = CNN_model(x_train,y_train,n_features)

x_test1 = np.expand_dims(x_test,axis=-1)
y_predict = model.predict_classes(x_test1)

y_predict = list(map(str, y_predict))
y_predict = [int(x) for x in y_predict]
print('准确率', metrics.accuracy_score(y_test, y_predict))
print('平均f1-score:', metrics.f1_score(y_test, y_predict, average='weighted'))



