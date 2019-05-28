coding utf-8

import sys
import codecs
import numpy as np
import pandas as pd
import tensorflow as tfimport keras
from keras_bert import load_trained_model_from_checkpoint,Tokenizer
from keras_bert.layers import MaskedGlobalMaxPool1D
from annoy import AnnoyIndex 
from sklearn.metric.pairwise import cosine_similarity
import logging 

def load_the_model():
    sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
    logging.info("this demo demonstrates how to load the pre-trained model and extract the sentence embedding with pooling")
    model_dir = "bert+dor"  ## need to check
    config_path, checkpoint_path,dict_path = model_dir + 'bert_config.json',model_dir + 'bert_model.ckpt', model_dir + 'vocab.txt'
    model = load_trained_model_from_checkpoint(config_path,checkpoint_path,seq_len=10)
    pool_layer = MaskedGloablMaxPool1D(name='Pooling')(model.output)
    model = keras.models.Model(inputs=model.inputs, outputs=pool_layer)
    token_dict = {}
    with codecs.open(dict_path, 'r','utf8') as reader:
        for line in reader:
            token = line.strip()
            token_dict[token] = len(token_dict)
    tokenizer = Tokenizer(token_dict)
    return tokenizer,model
