import json
import os
data_dir="/home/davidyu/gits/chinese-xinhua/data"
f = open(os.path.join(data_dir,"word.json"), encoding='utf-8')
word_list = json.load(f)

a1=word_list[0]
ch_word=[x['word'] for x in word_list]

print(ch_word[0:100])
