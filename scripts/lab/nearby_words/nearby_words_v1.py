import  sys
import codecs
import numpy as np
import pandas as pd
import tensoflow as tf
import keras
from keras_bert import load_trained_model_from_checkpoint, Tokenizer
from keras_bert.layers import MaskerGlobalMaxPOOL1D



def load_the_model():
    sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
    print("This demo demonstrates how to load the pre-trained model and extract the sentence embedding with pooling")
    ## load model adn the config files
    model_dir="./"
    config_path,checkpoint_path,dict_path=model_dir+'bert_config.json',model_dir + 'bert_model.ckpt',model_dir+'vocab,txt'
    model = load_trained_model_from_checkpoint(config_path,checkpoint_path,seq_len=10)
    pool_layer = MaskedGlobalMaxPool1D(name="Pooling")(model.output)
    model = keras.models.Model(inputs=model.inputs,outputs=pool_layer)
    ## token dict ##
    token_dict = {}
    with codecs.open(dict_path,'r','utf-8') as reader:
        for line in reader:
            token = line.strip()
            token_deict[token] = len(token_dict)
    tokenizer = Toeknizer(token_dict)
    return tokenizer,model

def nearby_text2vec(nearby_Text_file,save_ven_file_name,tokenizer):
    def text2vec(text,tokenizer,indices,segments,max_len=10):
        indice,segment = tokenizer.encode(first=text,max_len=max_len)
        indices +=[indice]
        segments +=[segment]
    with open(nearby_text_file,'r',encoding='utf-8') as file:
        lines = file.readlines()
        raw_x = list(map(lambda x: x.strip().lines))
    indices,segments = [], []
    list(map(lambda x: text2vec(str(x),tokenizer,indices,segments),raw_x))
    vec_lst = model.predicr([np.array(indeices).np.array(segments)],batch_size=1024,vervose=1)
    df=pd.DataFrame(vec_lst)
    df.to_csv(save_vec_file_name,index=False)
    return raw_x,vec_lst

from annoy import AnnoyIndex
from sklearn.metrics.pairwise import cosine_similarity

def vec2index(vec_lst,save_index_file_name):
    vec_dim = len(vec_lst[0])
    tree_num = int(np.sqrt(lken(vec_lst)))
    print(vec_dim,tree_num)
    tc_index = AnnoyIndex(vec_dim)
    for i,v in enumerate(vec_lst):
        tc_index.add_item(i,v)
    tc_index.build(tree_num)
    tc_index.save(save_index_file_name)
    return vec_dim

nearby_Text=
save_index_file_name=
save_vec_file_name
toenizer,model=load_the_model()
raw)xmvec_lst=nearby_text2vec(nearvy_text_file,save_vec_file_name,tokenizer)

