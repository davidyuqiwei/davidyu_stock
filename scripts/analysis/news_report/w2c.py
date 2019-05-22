import jieba
from gensim.models import word2vec
def clearSen(comment):
    comment = comment.strip(' ')
    comment = comment.replace('、','')
    comment = comment.replace('~','。')
    comment = comment.replace('～','')
    comment = comment.replace('{"error_message": "EMPTY SENTENCE"}','')
    comment = comment.replace('…','')
    comment = comment.replace('\r', '')
    comment = comment.replace('\t', ' ')
    comment = comment.replace('\f', ' ')
    comment = comment.replace('/', '')
    comment = comment.replace('、', ' ')
    comment = comment.replace('/', '')
    comment = comment.replace(' ', '')
    comment = comment.replace(' ', '')
    comment = comment.replace('_', '')
    comment = comment.replace('?', ' ')
    comment = comment.replace('？', ' ')
    comment = comment.replace('了', '')
    comment = comment.replace('➕', '')
    return comment
comment = open('test.txt').read()
comment = ' '.join(jieba.cut(comment))

fo = open("afterSeg.txt","w")
fo.write(comment)
print("finished!")
fo.close()

sentences=word2vec.Text8Corpus(u'afterSeg.txt')

model=word2vec.Word2Vec(sentences,min_count=3, size=50, window=5, workers=1)

