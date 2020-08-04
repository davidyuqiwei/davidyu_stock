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


def cnn_model(x_train_padded_seqs, y_train, x_test_padded_seqs, y_test,vocab):
    model = Sequential()
    #model.add(Embedding(len(vocab) + 1, 300, input_length=50)) #使用Embeeding层将每个词编码转换为词向量
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
    model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
    one_hot_labels = keras.utils.to_categorical(y_train, num_classes=3)  # 将标签转换为one-hot编码
    model.fit(x_train_padded_seqs, one_hot_labels,epochs=5, batch_size=800)
    return model

if __name__=='__main__':
    dataset = pd.read_excel("test.xlsx")
    cw = lambda x: list(jieba.cut(x))
    dataset['words'] = dataset['tt'].apply(cw)
    tokenizer=Tokenizer()  #创建一个Tokenizer对象
    #fit_on_texts函数可以将输入的文本中的每个词编号，编号是根据词频的，词频越大，编号越小
    tokenizer.fit_on_texts(dataset['words'])
    vocab=tokenizer.word_index #得到每个词的编号
    x_train, x_test, y_train, y_test = train_test_split(dataset['words'], dataset['label'], test_size=0.1)
    # 将每个样本中的每个词转换为数字列表，使用每个词的编号进行编号
    x_train_word_ids=tokenizer.texts_to_sequences(x_train)
    x_test_word_ids = tokenizer.texts_to_sequences(x_test)
    #序列模式
    # 每条样本长度不唯一，将每条样本的长度设置一个固定值
    x_train_padded_seqs=pad_sequences(x_train_word_ids,maxlen=50) #将超过固定值的部分截掉，不足的在最前面用0填充
    x_test_padded_seqs=pad_sequences(x_test_word_ids, maxlen=50)
    model = cnn_model(x_train_padded_seqs, y_train, x_test_padded_seqs, y_test,vocab)
    y_predict = model.predict_classes(x_test_padded_seqs)  # 预测的是类别，结果就是类别号
    y_predict = list(map(str, y_predict))
    y_predict = [int(x) for x in y_predict]
    print('准确率', metrics.accuracy_score(y_test, y_predict))
    print('平均f1-score:', metrics.f1_score(y_test, y_predict, average='weighted'))


