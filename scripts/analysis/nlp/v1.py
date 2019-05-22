# �˺��������ǶԳ�ʼ���Ͻ��зִʴ������Ϊѵ��ģ�͵�����
def cut_txt(old_file):
    import jieba
    global cut_file     # �ִ�֮�󱣴���ļ���
    cut_file = old_file + '_cut.txt'

    try:
        fi = open(old_file, 'r', encoding='utf-8')
    except BaseException as e:  # ��BaseException�����д���Ļ��࣬�������Ի�����д�������
        print(Exception, ":", e)    # ׷�ٴ�����ϸ��Ϣ

    text = fi.read()  # ��ȡ�ı�����
    new_text = jieba.cut(text, cut_all=False)  # ��ȷģʽ
    str_out = ' '.join(new_text).replace('��', '').replace('��', '').replace('��', '').replace('��', '') \
        .replace('��', '').replace('��', '').replace('��', '').replace('��', '').replace('��', '').replace('��', '') \
        .replace('��', '').replace('��', '').replace('��', '').replace('��', '').replace('��', '') \
        .replace('��', '')     # ȥ��������
    fo = open(cut_file, 'w', encoding='utf-8')
    fo.write(str_out)
def model_train(train_file_name, save_model_file):  # model_file_nameΪѵ�����ϵ�·��,save_modelΪ����ģ����
    from gensim.models import word2vec
    import gensim
    import logging
    # ģ��ѵ�������ɴ�����
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    sentences = word2vec.Text8Corpus(train_file_name)  # ��������
    model = gensim.models.Word2Vec(sentences, size=200)  # ѵ��skip-gramģ��; Ĭ��window=5
    model.save(save_model_file)
    model.wv.save_word2vec_format(save_model_name + ".bin", binary=True)   # �Զ��������ͱ���ģ���Ա�����
from gensim.models import word2vec
import os
import gensim

# if not os.path.exists(cut_file):    # �ж��ļ��Ƿ���ڣ��ο���https://www.cnblogs.com/jhao/p/7243043.html
cut_txt('����������.txt')  # ��ע���ļ����������Ϊutf-8�����ʽ

save_model_name = '����������.model'
if not os.path.exists(save_model_name):     # �ж��ļ��Ƿ����
    model_train(cut_file, save_model_name)
else:
    print('��ѵ��ģ���Ѿ����ڣ������ٴ�ѵ��')

# ������ѵ���õ�ģ��
model_1 = word2vec.Word2Vec.load(save_model_name)
# ���������ʵ����ƶ�/��س̶�
y1 = model_1.similarity("����", "ΤһЦ")
print(u"������ΤһЦ�����ƶ�Ϊ��", y1)
print("-------------------------------\n")

# ����ĳ���ʵ���ش��б�
y2 = model_1.most_similar("������", topn=10)  # 10������ص�
print(u"������������صĴ��У�\n")
for item in y2:
    print(item[0], item[1])
print("-------------------------------\n")
