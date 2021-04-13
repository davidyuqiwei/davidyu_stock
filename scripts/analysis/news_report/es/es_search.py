from body_match import *
from davidyu_cfg import *
from datetime import datetime
from elasticsearch import Elasticsearch
from collections import Counter
import re
from make_search_body import *



# ["豌豆蛋白" , "人造肉 ","养老院","电子烟","行业领军","氢能源"]
keyword = "电子烟"
body2 = make_search_body(keyword,"2019-01-01","2020-12-31",10000)

es = Elasticsearch()
ret = es.search(index="news_report",body=body2)
a1 = ret["hits"]["hits"]
stk_list = [ x.get("_source").get("stock_index") for x in a1  ]
text_list = [ x.get("_source").get("text") for x in a1  ]
dt_list = [ x.get("_source").get("dt") for x in a1  ]
id_list = [ x.get("_id") for x in a1  ]


search_str = ".{0,20}%s.{0,50}"%(keyword)

key_sentence_list = ['__'.join(re.findall(search_str,x)) for x in text_list]

df_list = [stk_list,dt_list,id_list,key_sentence_list]
df2 = pd.DataFrame(df_list).T
df2.columns = ["stock_index","dt","id","key_sentence"]
print(df2)

df3 = df2.groupby("stock_index").count().sort_values("dt")
print(df3)
#ret = es.search(index="news_report",body=body)
#a1 = ret["hits"]["hits"]


#c = Counter(stk_list)

#c.most_common()
