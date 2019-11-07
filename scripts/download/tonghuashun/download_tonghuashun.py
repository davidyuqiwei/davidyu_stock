from davidyu_cfg import *
from functions.connect_url import url_opener,driver_open
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist
from functions.get_datetime import *
from functions.save_DataFrame import save_the_table
def get_data(soup_text):
    a3 = soup_text.get_text() 
    a4 = a3.split("\n")
    a5 = [x.replace(' ','').replace('\t','') for x in a4 if x != '']
    return a5

def data_to_DF(all_tr):
    loop_len = len(all_tr)
    data_in = []
    for i in range(1,loop_len):
        data1 = get_data(all_tr[i])
        data_in.append(data1)
    ## to DataFrame
    df1 = pd.DataFrame(data_in)
    return df1

if __name__=='__main__':
    html = "http://data.10jqka.com.cn/financial/yjyg/"
    now_date,now_date_time = get_the_datetime()
    save_dir = data_dict.get("tonghuashun")
    soup2 = driver_open(html,"gbk")
    #soup2 = url_opener(html)
    t3 = soup2.findAll(attrs={'class':'page-table'})
    all_tr = t3[0].findAll('tr')  
    df_table = data_to_DF(all_tr)
    save_the_table(df_table,save_dir,now_date,now_date_time)
    

    html = 'http://data.10jqka.com.cn/rank/cxg/'
    soup2 = driver_open(html,"gbk")
    t3 = soup2.findAll(attrs={'class':'page-table'})
    all_tr = t3[0].findAll('tr')
    df_table = data_to_DF(all_tr)
    save_the_table(df_table,save_dir,now_date,now_date_time,'cxg')

'''
a2 = a1[1]
a3 = a2.get_text() 
a4 = a3.split("\n")
a5 = [x.replace(' ','').replace('\t','') for x in a4 if x != '']

'''

#print(soup2)
#table = soup2.find_all('table')[0]
#print(table)

