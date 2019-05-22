from keras.models import Sequential
from keras.layers import Dense, Activation

from keras.layers import Dense
from keras.datasets import cifar10

#https://github.com/nzw0301/keras-examples/blob/master/CNN_CIFAR10.ipynb

batch_size = 256
nb_classes = 10
epochs = 4
nb_filter = 10

img_rows, img_cols = 32, 32
img_channels = 3

## load the train data
(X_train, y_train), (X_test, y_test) = cifar10.load_data()
print('X_train shape:', X_train.shape)
print(X_train.shape[0], 'train samples')
print(X_test.shape[0], 'test samples')

X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255

### fasttext
from keras.datasets import imdb
max_features = 5000
maxlen = 400
batch_size = 32
embedding_dims = 20


(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)

print(len(x_train), 'train sequences')
print(len(x_test), 'test sequences')

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



model.add(Dense(units=64, activation='relu', input_dim=100))
model.add(Dense(units=10, activation='softmax'))

model.compile(loss='categorical_crossentropy',
        optimizer='sgd',
        metrics=['accuracy'])
model.fit(x_train, y_train, epochs=5, batch_size=32)

'''
model = Sequential([
    Dense(32, input_shape=(784,)),
    Activation('relu'),
    Dense(10),
    Activation('softmax'),
])

'''
