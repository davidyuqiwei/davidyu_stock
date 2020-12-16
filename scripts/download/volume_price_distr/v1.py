import sys
from davidyu_cfg import *
from functions.connect_url import url_opener



def download_volume_price_distr(stock_index):
    if stock_index[0] == '6':
        start_string = 'sh'
    else:
        start_string = 'sz'
    html1 = "https://vip.stock.finance.sina.com.cn/quotes_service/view/cn_price.php?symbol="+start_string+stock_index
    soup2 = url_opener(html1)
    
    soup_out = soup2.findAll('tr',attrs={'class','gray'})
    soup_out = soup2.findAll('td')
    
    data1 = []
    for i in soup_out:
        try:
            a1 = float(i.get_text())
            data1.append(a1)
        except:
            pass
    
    out_list = []
    for i in range(0,len(data1),2):
        b = data1[i:i+2]
        out_list.append(b)
    df2= pd.DataFrame(out_list)
    df2.columns = ["price","vol"]
    df2.to_csv(stock_index+".csv",index=0)
    return df2
if __name__ == "__main__":
    import time 
    stock_index_list = ["300053","002967","002911","300684","600260"]
    for i in stock_index_list:
        download_volume_price_distr(i)
        time.sleep(3)

