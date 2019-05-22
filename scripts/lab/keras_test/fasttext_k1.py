### fasttext
#   https://github.com/nzw0301/keras-examples/blob/master/fasttext.ipynb
import numpy as np
np.random.seed(1337)

from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Embedding, GlobalAveragePooling1D
from keras.datasets import imdb
max_features = 5000
maxlen = 400
batch_size = 32
embedding_dims = 20

### download data and save to npy
'''
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)
np.save("x_train.npy",x_train)
np.save("y_train.npy",y_train)
np.save("x_test.npy",x_test)
np.save("y_test.npy",y_test)
'''
print(len(x_train), 'train sequences')
print(len(x_test), 'test sequences')


x_train=np.load("x_train.npy")
y_train=np.load("y_train.npy")
x_test=np.load("x_test.npy")
y_test=np.load("y_test.npy")

x_train = sequence.pad_sequences(x_train, maxlen=maxlen)
x_test = sequence.pad_sequences(x_test, maxlen=maxlen)

model = Sequential()
model.add(Embedding(input_dim=5000, output_dim=embedding_dims))
model.add(GlobalAveragePooling1D())
model.add(Dense(1, activation='sigmoid'))


model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

model.fit(x_train, y_train,
          batch_size=batch_size,
          validation_data=(x_test, y_test))




#######################################################
