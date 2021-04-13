import sys
from davidyu_cfg import *
from functions.connect_url import url_opener
from functions.data_dir import *
from functions.get_datetime import *
from functions.common.save_DataFrame import save_df_date
import time
def save_file_name(save_dir,file_name_in,now_date=None):
    if now_date is None:
        now_date,now_date_time = get_the_datetime()
    file_name = file_name_in +'_' + now_date+'.csv'
    save_file = os.path.join(save_dir,file_name)
    return save_file

def download_volume_price_distr(stock_index,now_dt):
    save_dir = data_dict.get("volume_price_distr")
    dir_name1 = os.path.join(save_dir,stock_index)
    out_file_name  = save_file_name(dir_name1,stock_index,now_dt)
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
        except Exception as e:
            logging.error(e)
            pass
    out_list = []
    for i in range(0,len(data1),2):
        b = data1[i:i+2]
        out_list.append(b)
    df2= pd.DataFrame(out_list)
    df2.columns = ["price","vol"]
    df2["stock_index"] = stock_index
    df2["dt"] = now_dt 
    save_dir = data_dict.get("volume_price_distr")
    dir_name1 = os.path.join(save_dir,stock_index)
    make_dir(dir_name1)
    save_df_date(dir_name1,stock_index,df2,now_dt)
    time.sleep(3.5)
    return df2
if __name__ == "__main__":
    import time
    stock_index = sys.argv[1]
    dt = sys.argv[2]
    stock_index = stock_index.zfill(6)
    try:
        download_volume_price_distr(stock_index,dt)
    except Exception as e:
        logging.error(e)
        logging.error(stock_index)
        pass



