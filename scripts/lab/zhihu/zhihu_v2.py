from functions import *
from bs4 import BeautifulSoup as BS


def download_zhihu_ques_search(question):
    url="https://www.zhihu.com/search?type=content&q="+question
    ## download the similar question in zhihu for the question we are interest
    cont1=driver_open(url)
    title_l1=cont1.find_all('span',attrs={'class',"Highlight"})    
    title=[]
    for ti in title_l1:
        str1=ti.get_text()
        title.append(str1)
    ## the url of the similar question 
    url_sub_question=cont1.find_all('a')
    urls=[]
    for ur in url_sub_question:
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
    return title,text


import pandas as pd
k=0
#question = ["铁锅炒菜能补铁吗","宝宝咋生的更聪明","孩子白头发","晚上什么时候运动比较好"]
question = ["宝宝头发如何长的快"]
for qu in question:
    title,text = download_zhihu_ques_search(qu) 
    df_list = {"title": title,
            "text": text
            }
    k+=1
    df = pd.DataFrame(df_list)
    file_name = "QA_zhihu_"+str(k)+".csv"
    #df.to_csv(file_name,index=0,encoding='utf_8_sig') 
print(df)




'''
url2='https://zhuanlan.zhihu.com/p/20481688'
cont2=driver_open(url2)


c1=cont2.find_all("div", attrs={'class',"RichText ztext Post-RichText"})
c2=c1[0]
c2.get_text()




a3['data-za-detail-view-id']
        ,attrs={'target',"_blank"})    

'''
