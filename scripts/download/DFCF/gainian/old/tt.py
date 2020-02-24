from davidyu_cfg import *
from functions.connect_url import url_opener

#soup2 = url_opener("http://data.eastmoney.com/xuangu/#Yz1bZ2Z6czYoQkswNDQ3KV18cz1nZnpzNihCSzA0NDcpfHN0PTE=")

#a1 = soup2.find_all('div',attrs={'style','display: none;'})


'''
a1 = soup2.find_all('ul')

gainian_id = []
for ul_list in a1[1:]:
    #a2 = a1[1]
    a3 = ul_list.find_all('li') 
    for i in a3:
        gainian_id.append(i.get('id'))

'''

