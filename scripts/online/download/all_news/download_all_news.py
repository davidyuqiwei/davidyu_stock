from davidyu_cfg import *
from functions.CxExtractor import CxExtractor
import sys
import os
from functions.connect_url import driver_open_noBS
script_dir = os.path.split(os.path.realpath(__file__))[0]
filename = os.path.basename(__file__)
print("the script path is "+script_dir)
os.chdir(script_dir)
from dir_control.data_dir_v1 import data_dict,stk_index_list
import time

'''
download news in the website
'''

### when update the news sources, be aware about the style of the json/ dict
stock_news = { 
    'sina': "https://finance.sina.com.cn/stock/",
    "dfcf": "http://finance.eastmoney.com/",
    "ifeng": "http://finance.ifeng.com/",
    "ftchinese": "http://www.ftchinese.com/channel/economy.html",
    "nature_researchAnalysis": "https://www.nature.com/research-analysis",
    "ifeng": "http://finance.ifeng.com/",
    "zdnet": "https://www.zdnet.com/",
    "xueqiu": "https://xueqiu.com/",
    "tonghuashun":"http://stock.10jqka.com.cn/",
    "science":"https://www.sciencemag.org/#",
    "usa_stock_news":"http://global.eastmoney.com/a/cmgsc.html",
    "sina_usa_stock":"https://finance.sina.com.cn/stock/usstock/"
}

'''

stock_news = {
    "dfcf_news":"http://finance.eastmoney.com/"
}
'''

## keys & website download use html driver
BS_KEY = ["xueqiu","tonghuashun"]



def get_text(key):
    raw_html = stock_news.get(key)
    if key in BS_KEY:
        html = driver_open_noBS(raw_html)
        #print(html)
    else:
        html = cx.getHtml(raw_html)
    content = cx.filter_tags(html)
    s = cx.getText(content)
    #print(s)
    # save dir
    dir_all_news = data_dict.get("all_news")
    today = time.strftime("%Y-%m-%d", time.localtime())
    file_name = key+"_"+today+".txt"
    files = os.path.join(dir_all_news,file_name)
    #print(files)
    f = open(files,'w+')
    print(s,file=f)
    f.close()
if __name__=='__main__':
	cx = CxExtractor(threshold=86)
	# html = cx.getHtml("http://www.bbc.com/news/world-europe-40885324")
	dir_all_news=data_dict.get("all_news")
	print(dir_all_news)
	for key in stock_news:
	    try:
	        get_text(key)
	    except:
	        print(key)
	        pass
	import datetime
	nowTime=datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
	print(nowTime+" finished "+os.path.join(script_dir,filename))
	os_str = "rm -rf %s/geckodriver.log" %script_dir
	print(os_str)
	os.system(os_str)
