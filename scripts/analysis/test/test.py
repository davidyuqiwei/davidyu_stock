import os
os.system("sh /usr/davidyu/tensorflow.sh")

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

