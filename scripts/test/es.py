import pandas as pd
a1 = pd.read_csv("/home/davidyu/stock/data/news_report/000088/000088_2012-03-19_2.txt")



file1 = "/home/davidyu/stock/data/news_report/000088/000088_2012-03-19_2.txt"
with open(file1) as f: ss = f.read()
text1 = ss.replace(" ","")

doc = {
    'author': 'david',
    'text': text1,
    'timestamp': datetime.now()
}
res = es.index(index="news_report", id="000088_2012-03-19_2", body=doc)
print(res['result'])

res = es.get(index="news_report", id="000088_2012-03-19_2")
print(res['_source'])


body = {
  "query":{
    "match":{
      "text":"长期"
    }
    "range":{
    
    }
  }
}

es.search(index="news_report",body=body)

# delete data
# es.delete(index='indexName', doc_type='typeName', id='idValue')

