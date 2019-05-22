import jieba

# new_text = jieba.cut(text, cut_all=False)
# global cut_file




def model_train(train_file_name, save_model_file):  # model_file_nameΪѵ????ϵ????,save_modelΪ???????
    from gensim.models import word2vec
    import gensim
    import logging
    # ģ?ѵ??????ɴ???
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    sentences = word2vec.Text8Corpus(train_file_name)  # ?????    
    model = gensim.models.Word2Vec(sentences, size=200)  # ѵ??skip-gramģ?; Ĭ?window=5
    model.save(save_model_file)
    model.wv.save_word2vec_format(save_model_name + ".bin", binary=True)   





def stopwordslist(filepath):  
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]  
    return stopwords  

def seg_sentence(sentence):  
    sentence_seged = jieba.cut(sentence.strip())  
    stopwords = stopwordslist('F:/davidyu/script/git/davidyu_stock/github_scripts/stopwords/hagongda.txt')  # 这里加载停用词的路径  
    outstr = ''  
    for word in sentence_seged:  
        if word not in stopwords:  
            if word != '\t':  
                outstr += word  
                outstr += " "  
    return outstr 
old_file="F:/stock/data/news/v1.txt"
fi = open(old_file, 'r', encoding='utf-8')
text = fi.read() 
# print(text)
str_out=seg_sentence(text)
# print(str_out)

cut_file = 'F:/davidyu/script/git/davidyu_stock/scripts/analysis/nlp/cut.txt'
fo = open(cut_file, 'w', encoding='utf-8')
fo.write(str_out)
fo.close()

save_model_name = 'a1.model'

from gensim.models import word2vec
model_train('F:\\davidyu\\script\\git\\davidyu_stock\\scripts\\analysis\\nlp\\cut.txt', save_model_name)

model_1 = word2vec.Word2Vec.load(save_model_name)
y2 = model_1.most_similar(u"经济", topn=20)  # 20个最相关的
print(u"和【经济】最相关的词有：\n")
for item in y2:
    print(item[0], item[1])
print(str_out)

# # y1 = model_1.similarity(u"经济", u"上涨")
# # print("【经济】和【上涨】的相似度为：", y1)

