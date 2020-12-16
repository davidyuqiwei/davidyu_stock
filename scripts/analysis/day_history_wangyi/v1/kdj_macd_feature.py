from davidyu_cfg import *
from functions.ForDownload import generate_stock_index,stk_index_list_gen
from functions.data_dir import *
#from dir_control.data_dir_v1 import data_dict
import time
from functions.make_dir import *
from functions.LinearReg import *
from functions.colNames import setColname
from functions.stockstats.stockStats import *
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist
from functions.get_datetime import *
from functions.day_history.dayHistoryFeature import dayHistoryFeature
#日期    开盘价  最高价  最低价  收盘价  涨跌额  涨跌幅(%)   
#成交量(手)  成交金额(万>元) 振幅(%)   换手率(%)

def loadData(data_dir,stock_index):
    df1 = pd.read_csv(os.path.join(data_dir,stock_index,stock_index+"_2020_3.csv"))
    df2 = pd.read_csv(os.path.join(data_dir,stock_index,stock_index+"_2020_4.csv"))
    df1 = pd.concat([df1,df2])
    df1.columns = setColname().day_history_wangyi()
    return df1

def allKdj(now_date,stock_index):
    stock_index_list = []
    j_line = []
    stock_date_list = []
    rsi_6 = []
    try:
        wy_data_dir = data_dict.get("day_history_wangyi")
        df1 = loadData(wy_data_dir,stock_index).sort_values("stock_date")
        stock = DF_to_StockDataFrame(df1)
        df_stock = stock_kdj(stock)
        kdj_j_today = np.round(df_stock['kdjj'][df_stock['date']==now_date].values[0],3)
        rsi_today = np.round(df_stock['rsi_6'][df_stock['date']==now_date].values[0],3)
        stock_index_list.append(stock_index)
        j_line.append(kdj_j_today)
        rsi_6.append(rsi_today)
        stock_date_list.append(now_date)
    except:
        pass
    return stock_index_list,j_line,stock_date_list,rsi_6
if __name__ == "__main__":
    now_date,now_date_time = get_the_datetime()
    now_date = now_date.replace('_','-')
    stock_index = sys.argv[1]
    now_date = sys.argv[2]
    #stock_index = '601398'
    #now_date = '2020-11-24'
    stock_index_list,j_line,stock_date_list,rsi_6 = allKdj(now_date,stock_index)
    df_kdj_out = pd.DataFrame([stock_date_list,stock_index_list,j_line,rsi_6]).T
    df_kdj_out.columns = ['stock_date','stock_index','kdjj','rsi_6']
    #print(df_kdj_out)
    df_kdj_out.sort_values('kdjj').to_csv('wy_kdj.csv',index=0,mode='a')



"""
def trade_close_price(df1):
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

"""




'''
dazong_date = "2020-02-20"
trade_close_price = trade_close_price(df1)
df3 = data_follow(df1,dazong_date)
next_day_change_ratio = next_day_change(df3,trade_close_price)
#print("next day change ratio: %f" %(next_day_change_ratio))
## next 5 days
df_next_5_days = next_day_close_price = df3.iloc[0:4]
t1 = LinearReg()
slope, inter = t1.single_linear_reg(df_next_5_days,"close")
#print("next 5 days change slope: %f" %(slope))
print("%f,%f,%s,%s"%(next_day_change_ratio,slope,stock_index,dazong_date))

'''






