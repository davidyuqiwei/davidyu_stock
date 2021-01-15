from davidyu_cfg import *
from datetime import datetime
from elasticsearch import Elasticsearch
#from body import *
data_dir = data_dict.get("news_report")


es = Elasticsearch()

def make_doc(text1,stock_index,dt):
    doc = {
        'author': 'david',
        'text': text1,
        'timestamp': datetime.now(),
        'dt':dt,
        'stock_index':stock_index
    }
    return doc
dirs = os.listdir(data_dir)
for d1 in dirs:
    if 'HIVE' not in d1:
	    files = os.listdir(os.path.join(data_dir,d1))
	    for f1 in files:
	        file_in = os.path.join(data_dir,d1,f1)
	        with open(file_in) as f: ss = f.read()
	        text1 = ss.replace(" ","")
	        stock_index = f1[0:6]
	        dt = f1[7:17]
	        doc = make_doc(text1,stock_index,dt)
	        res = es.index(index="news_report", id=f1.replace(".txt",""), body=doc)
    print('aaaa'+d1)

'''
doc = ret['hits']['hits']
stock_index_list = []
for item in doc:
    stock_index_list.append(item.get("_source").get("stock_index"))

'''
#ret = es.get_source(index="news_report",id='600798_2017-03-06_1')
#ret = es.search(index="news_report",body=body)






