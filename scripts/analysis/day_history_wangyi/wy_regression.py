from davidyu_cfg import *
from functions.ForDownload import generate_stock_index,stk_index_list_gen
from functions.data_dir import *
#from dir_control.data_dir_v1 import data_dict
import time
from functions.make_dir import *
from functions.LinearReg import *
#data_dir = data_dict.get("day_history_wangyi")

#日期    开盘价  最高价  最低价  收盘价  涨跌额  涨跌幅(%)   成交量(手)  成交金额(万>元) 振幅(%)   换手率(%)



def Trade_close_price(df1,dazong_date):
    trade_close_price = df1[df1['stock_date'] == dazong_date].close.values[0]
    return trade_close_price


def next_day_change(df3,trade_close_price):
    next_day_close_price = df3.iloc[0].close
    change_ratio = round((next_day_close_price - trade_close_price)/trade_close_price,2)
    #print(change_ratio)
    return change_ratio

def data_follow(df1,dazong_date):
    df2 = df1[df1['stock_date'] > dazong_date]
    df3 = df2.sort_values("stock_date")
    return df3
def data_columns():
    cols = ['stock_date','open','high','low','close','change_price','change_ratio','trade_num','trade_price','variatio','turnover_rate','stock_index']
    return cols




def get_reg_change(stock_index,dazong_date):
    data_dir = data_dict.get("day_history_wangyi")
    df1 = pd.read_csv(os.path.join(data_dir,stock_index,stock_index+"_2020_1.csv"))
    df1.columns = data_columns()
    
    #dazong_date = "2020-02-20"
    trade_close_price = Trade_close_price(df1,dazong_date)
    df3 = data_follow(df1,dazong_date)
    next_day_change_ratio = next_day_change(df3,trade_close_price)
    #print("next day change ratio: %f" %(next_day_change_ratio))
    ## next 5 days
    df_next_5_days = next_day_close_price = df3.iloc[0:4]
    t1 = LinearReg()
    slope, inter = t1.single_linear_reg(df_next_5_days,"close")
    #print("next 5 days change slope: %f" %(slope))
    #print("%f,%f,%s,%s"%(next_day_change_ratio,slope,stock_index,dazong_date))
    return [next_day_change_ratio,slope,stock_index,dazong_date]
if __name__ =='__main__':
    data_dir = "/home/davidyu/stock/data/tmp/dazong_data"
    #stock_index = sys.argv[1]
    stock_list_df = pd.read_csv(os.path.join(data_dir,"all.csv"))
    #get_reg_change("002570","2020-01-02")
    stock_index_list = stock_list_df.SECUCODE.tolist()
    dazong_date_list = stock_list_df.trade_date.tolist()
    return_list = []
    for i in range(0,len(stock_index_list)):
        try:
            all_list = get_reg_change(str(stock_index_list[i]).zfill(6),dazong_date_list[i])
            return_list.append(all_list)
        except:
            pass




