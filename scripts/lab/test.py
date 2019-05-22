from CxExtractor import CxExtractor
import sys
sys.path.append("../")
from dir_control.data_dir_v1 import data_dict,stk_index_list
import os


cx = CxExtractor(threshold=186)
# html = cx.getHtml("http://www.bbc.com/news/world-europe-40885324")
html = cx.getHtml("https://finance.sina.com.cn/stock/")
#html = cx.getHtml("http://www.eastmoney.com/")
content = cx.filter_tags(html)
s = cx.getText(content)
#print(s)
dir_all_news=data_dict.get("all_news")
files=os.path.join(dir_all_news,"test.txt")
f = open(files, 'w+')

print(s, file=f)

