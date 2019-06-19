# -*- coding: UTF-8 -*-
## this script translate the string using baidu api
import time
import os 
#import md5
import urllib
import random
import json
import hashlib



def make_the_url(text,fromLang,toLang):
    #text = "你好"
    myurl = "http://api.fanyi.baidu.com/api/trans/vip/translate?"
    #fromLang = 'zh'#繁体
    #fromLang='auto'#自动检测
    #toLang='en'
    salt=random.randint(32768,65536)
    ###
    str1=appid+text+str(salt)+secretKey
    m=hashlib.md5()
    m.update(str1.encode(encoding='utf-8'))
    sign = m.hexdigest()
    myurl=myurl+'q='+text+'&from='+fromLang+'&to='+toLang+'&appid='+appid+'&salt='+str(salt) + '&sign=' + sign
    #print(myurl)
    return myurl

## the input
appid = "20190613000307070"
secretKey = "C0hmuBM4vML3_5WcgJdi"

text = """Melanie Wolkoff Wachsman in CloudNew customer expectations are rewriting the digital transformation playbookCustomers expect constant innovation. We are now entering an era where a company’s ability to provide innovative experiences is as important as the quality of its products. New 2019 research found that 84% of customers now consider these factors equally when deciding who to buy from.13 hours ago
 Vala Afshar in Digital Transformation
 """
fromL = "en"
toL = "zh"
### make url and download from the url
myurl = make_the_url(text,fromL,toL)
download_str = "wget -O %s '%s'"%("trans.txt",myurl)
print(download_str)
os.system(download_str)
## open the download file and get the result 
f = open('trans.txt')
result = f.read()
result1 = json.loads(result)
trans_result = result1['trans_result'][0]['dst']
print(trans_result)

#res2 = urllib.request.urlopen(myurl)

#response = opener.open(url)





#opener.addheaders = [('User-agent', 'Mozilla/5.0')]
#response = opener.open(url)

'''
httpClient = httplib.HTTPConnection('api.fanyi.baidu.com')
httpClient.request('GET', myurl)

'''

