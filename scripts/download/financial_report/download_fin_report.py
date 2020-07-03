#from functions import *
from davidyu_cfg import * 
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist
from functions.connect_url import url_opener
from functions.make_dir import make_dir
import eventlet
from functions.html_list import *
import traceback
eventlet.monkey_patch()
"""
this sript download all the finical data in sina
"""
def find_url(url):
    soup2 = url_opener(url)
    a1 = soup2.find_all(id='BalanceSheetNewTable0')
    soup1 = a1[0]
    return soup1

def download_table(html,stock_index,year,save_dir):
    #print(html)
    soup1 = find_url(html)
    rows = soup1.find_all('tr')
    data = []
    for row in rows:
        cols=row.find_all('td')
        cols = [ele.text.strip() for ele in cols] ## get every data in the rows
        data.append([ele for ele in cols if ele]) ## make a list for data to save
        #print cols
    #print(data)
    data1 = pd.DataFrame(data)
    return data1

def trans_data(df):
    '''
    trans the string "--" to -9999 for save the data
    and give the column name
    '''
    df1 = df.replace("--",-9999).fillna(-9999)
    df1 = df1.T
    df1.columns = df.T.iloc[0].tolist()  #column to row
    df2 = df1.iloc[1:,1:]  ## rows 1:,  columns 1:
    return df2

def main_process(stock_index,year,save_dir,file_name):
    ## download data
    html1 = html_content().html_financial_report_source(stock_index,year)
    df = download_table(html1,stock_index,str(year),save_dir)
    ### trans data
    df_tr = trans_data(df)
    df_tr['stock_index'] = stock_index
    ## save data
    df_tr.to_csv(file_name,index=0)
    return 1

def make_filename_check_if_exists(save_dir,stock_index,year):
    save_dir2 = os.path.join(save_dir,stock_index)
    make_dir(save_dir2)
    file_name = os.path.join(save_dir2,stock_index+'_'+str(year)+'.csv')
    if_exists = os.path.exists(file_name)  ## True or False
    return file_name,if_exists


def do_download(stock_index,year,save_dir,file_name,if_file_exists):
    try:
        status = main_process(stock_index,year,save_dir,file_name)
        print("download file "+file_name)
    except Exception:
        print("failed_"+file_name)
        traceback.print_exc()
def loop_for_download_fin_report(stock_index,year_range):
    save_dir = data_dict.get("financial_report")
    for year in year_range:
        file_name,if_file_exists = make_filename_check_if_exists(save_dir,stock_index,year)
        if if_file_exists == False:
            with eventlet.Timeout(2.7,False):
                do_download(stock_index,year,save_dir,file_name,if_file_exists)
                time.sleep(20)
        else:
            pass
if __name__ =='__main__':
    start_year = 2019
    end_year = 2020
    year_range = range(start_year,end_year+1)
    stock_index = sys.argv[1]
    loop_for_download_fin_report(stock_index,year_range)
    #dir_fin_report = data_dict.get("financial_report")

            
