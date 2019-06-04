from functions import *
from bs4 import BeautifulSoup as BS
url="https://www.zhihu.com/search?type=content&q=%E7%B3%96%E5%B0%BF%E7%97%85%E4%BA%BA%E5%A6%82%E4%BD%95%E4%B9%B0%E4%BF%9D%E9%99%A9"

url="https://www.zhihu.com/search?type=content&q="+"糖尿病人如何买保险"
cont1=driver_open(url)

#a1=cont1.find_all('div',attrs={'class','blk_container'})


title_l1=cont1.find_all('span',attrs={'class',"Highlight"})    
title=[]
for ti in title_l1:
    str1=ti.get_text()
    title.append(str1)


#url_l1=cont1.find_all('a',attrs={'target',"_blank"})    

url_l1=cont1.find_all('a')

urls=[]
for ur in url_l1:
    try:
	    check_num=ur['data-za-detail-view-id'] 
	    if check_num == '3942':
	        url_in=ur['href']
            if 'zhuanlan' in url_in:
                urls.append("https:"+url_in)
            elif 'question' in url_in:
                urls.append("https://www.zhihu.com"+url_in)
	    else:
	        pass
    except:
        pass

text=[]
for u2 in urls:
    cont2 = driver_open(u2)
    try:
	    if 'zhuanlan' in u2:
		    #cont2 = driver_open(u2)
		    c1=cont2.find_all("div", attrs={'class',"RichText ztext Post-RichText"})
		    c2=c1[0]
		    tt=c2.get_text()
		    text.append(tt)
	    else:
	        c1=cont2.find_all("div",attrs={'class',"RichContent RichContent--unescapable"})
	        c2=c1[0]
	        tt=c2.get_text()
	        text.append(tt)
    except:
        text.append('no')
        pass

import pandas as pd
df_list = {"title": title,
        "text": text
        }
pd.DataFrame(df_list)



url2='https://zhuanlan.zhihu.com/p/20481688'
cont2=driver_open(url2)


c1=cont2.find_all("div", attrs={'class',"RichText ztext Post-RichText"})
c2=c1[0]
c2.get_text()




a3['data-za-detail-view-id']
        ,attrs={'target',"_blank"})    



