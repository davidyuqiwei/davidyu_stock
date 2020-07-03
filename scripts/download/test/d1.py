import sys
from davidyu_cfg import *
from functions.connect_url import url_opener

html1 = "http://vip.stock.finance.sina.com.cn/corp/go.php/vCI_CorpInfo/stockid/002079.phtml"
soup2 = url_opener(html1)
#print(soup2)
soup_out = soup2.find_all(attrs={'class','tagmain'})
soup_out = soup_out[0].find_all("tr")
print(soup_out[0])

text_list = []
keys = []
for i in soup_out:
    a2 = i.text.strip()
    try:
        text_list.append(a2.replace("：",":").split(":")[1])
        keys.append(a2.replace("：",":").split(":")[0])
    except:
        pass
