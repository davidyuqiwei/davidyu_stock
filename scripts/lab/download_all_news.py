from CxExtractor import CxExtractor
import sys
import os
script_dir=os.path.split(os.path.realpath(__file__))[0]
print("the script path is "+script_dir)
## change the work dir to the script dir
os.chdir(script_dir)
up_dir=os.path.abspath(os.path.join(os.getcwd(), "../"))
print("the up dir is "+ up_dir)
sys.path.append(up_dir)
from dir_control.data_dir_v1 import data_dict,stk_index_list
import time


stock_news = { 
    'sina': "https://finance.sina.com.cn/stock/",
    "dfcf": "https://finance.sina.com.cn/stock/",
<<<<<<< HEAD
    "ifeng": "http://finance.ifeng.com/",
    "ftchinese": "http://www.ftchinese.com/channel/economy.html",
    "nature_researchAnalysis": "https://www.nature.com/research-analysis"
=======
    "ifeng": "http://finance.ifeng.com/"
>>>>>>> 1f748b377819d67350ada8ca8130fda7752e2a91
}



cx = CxExtractor(threshold=86)
# html = cx.getHtml("http://www.bbc.com/news/world-europe-40885324")
dir_all_news=data_dict.get("all_news")
print(dir_all_news)

def get_text(key):
    raw_html = stock_news.get(key)
    html = cx.getHtml(raw_html)
    content = cx.filter_tags(html)
    s = cx.getText(content)
    #print(s)
    # save dir
    dir_all_news=data_dict.get("all_news")
    today=time.strftime("%Y-%m-%d", time.localtime())
    file_name = key+"_"+today+".txt"
    files=os.path.join(dir_all_news,file_name)
    print(files)
    f=open(files,'w+')
    print(s,file=f)
for key in stock_news:
    get_text(key)
