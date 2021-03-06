'''
this script download 
all the owner  data 
'''
import sys
from davidyu_cfg import *
from functions.connect_url import url_opener


def download_html_to_df(html1):
    '''
    download html do DataFrame,
    @input: a html url,
    @output: a pandas DataFrame
    '''
    soup2 = url_opener(html1)
    soup_out = soup2.findAll('a',href=True)
    ## get date, which '2018-10-30' start with #2
    dates_in = [dates_str['href'][1:11] for dates_str in soup_out if dates_str['href'].startswith("#2")]
    tr_str = soup2.findAll('tr')
    #a1=t3[10]
    #------------------------------------------------------------#
    #--------- prase log to data ----------------------#
    data=[]
    for a1 in tr_str:
        cols = a1.findAll('td')
        cols = [ele.text.strip() for ele in cols]
        publish_date = '2099-01-01'
        if len(cols)==2:
            if cols[0] == '公告日期':
                publish_date = cols[1]
        else:
            pass
        if len(cols) == 5:
            data.append([ele for ele in cols if ele] + [publish_date])
        else:
            pass
    #print(data)
    import pandas as pd
    data1 = pd.DataFrame(data)
    data1.columns = ['index_in','owner_name','amount','ratio','character','publish_date']
    #--------------------------------------------------------------------#
    #------- make date date align with data
    #data1.index_in.value_counts()
    date_all=[]
    k=-1
    for index1 in data1.index_in:
        if index1=='1':
            k+=1
        dates_in1 = dates_in[k]
        date_all.append(dates_in1)
    data1['date'] = date_all
    return data1
#### transform to chinese
def tr(x):
    x1 = x.encode('latin1',"ignore").decode('gb2312',"ignore")
    return x1
def _transform_data(data_in):
    ## some data will be NA fill it
    data_in['character'] = data_in['character'].fillna('david')
    data_in['owner_name'] = data_in['owner_name'].fillna('david')
    data_in['owner_name'] = data_in['owner_name'].apply(tr)
    data_in['character'] = data_in['character'].apply(tr)
    data2=data_in
    return data2
def save_data(data1,save_dir,stock_index):
    import os
    file_name = stock_index+'.csv'
    save_file_name = os.path.join(save_dir,file_name)
    data1.to_csv(save_file_name,index=0,header=None)
def check_data(df):
    ## check data if need to re-encode
    c1=sum(df["owner_name"]=="")
    c2=sum(df["owner_name"]=="()")
    return c1+c2
def get_html(stock_index):
    html1='http://vip.stock.finance.sina.com.cn/corp/go.php/vCI_CirculateStockHolder/stockid/%s/displaytype/3000.phtml' %stock_index
    return html1
def process(stock_index,dir_liutong_owner):
    html1 = get_html(stock_index)
    data1 = download_html_to_df(html1)
    data1['stock_index'] = stock_index
    data_raw=data1.copy(deep=True)
    '''
    -if na fill with 'david'
    -if it is latin1 transform to gb2312
    '''
    data2 = _transform_data(data1)
    check_tr_data = check_data(data2)
    '''
    if data need to re-encode, 
    if yes save the re-encode data
    else save the raw data
    '''
    if check_tr_data>1:
        save_data(data_raw,dir_liutong_owner,stock_index)
    else:
        save_data(data2,dir_liutong_owner,stock_index)

def main(stock_index):
    #from davidyu_cfg import *
    from dir_control.data_dir_v1 import data_dict,stk_index_list
    import time
    dir_liutong_owner = data_dict.get("liutong_owner")
    #dir_liutong_owner = data_dict.get("tmp")
    k=0
    #stk_index_list=['000011','000014']
    try:
        process(stock_index,dir_liutong_owner)
    except:
        print(stock_index)
        pass

if __name__ == '__main__':
    stock_index = sys.argv[1]
    main(stock_index)




'''
#data1.iloc[1:]

stock_index='000917'
html1='http://vip.stock.finance.sina.com.cn/corp/go.php/vCI_CirculateStockHolder/stockid/%s/displaytype/300.phtml' %stock_index
data1=down(html1)

data1['owner_name']=data1['owner_name'].apply(tr)
data1['character']=data1['character'].apply(tr)
data1.to_csv("test1.csv",index=0)

#data1.to_csv("test.csv",encoding="latin1")
#a1=t3[4:17]

'''
