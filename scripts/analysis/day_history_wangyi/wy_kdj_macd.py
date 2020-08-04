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
    df1 = pd.read_csv(os.path.join(data_dir,stock_index,stock_index+"_2020_2.csv"))
    df2 = pd.read_csv(os.path.join(data_dir,stock_index,stock_index+"_2020_3.csv"))
    df1 = pd.concat([df1,df2])
    df1.columns = setColname().day_history_wangyi()
    return df1


def getFeatture(stock_index):
    wy_data_dir = data_dict.get("day_history_wangyi")
    df1 = loadData(wy_data_dir,stock_index).sort_values("stock_date")
    stock = DF_to_StockDataFrame(df1)
    df_stock = stock_kdj(stock)
    #df_kdj_macd['adj_close'] = df_kdj_macd["macd"] 
    df_class = dayHistoryFeature.makeHistoryFeature(df_stock,10,"macdh")
    df_kdj_macd = df_class.df_out
    macd_feature_name = df_class.new_history_days_colname
    return df_kdj_macd,macd_feature_name

stock_index = "601398"
df_out,macd_feature_name = getFeatture(stock_index)

seq = df_out["macdh"].tolist()
pos_days = []
neg_days = []

cut = 0
seq_list = []
for i, element in enumerate(seq):
    if seq[i] * seq[i+1] <0:
        seq_list.append(seq[cut:(i+1)])
        cut = i+1
    else:
        pass

days_cnt = []
ext_val = []
for x in seq_list:
    if np.mean(x)>0:
        cnt_dir = 1
        ext_val.append(np.round(np.max(x),3))
    else:
        cnt_dir = -1
        ext_val.append(np.round(np.min(x),3))
    days_cnt.append(len(x) * cnt_dir)








def allKdj(now_date):
    stock_index_list = []
    j_line = []
    stock_date_list = []
    for i in stk_index_list:
        if i[0:2] == '60' or i[0] == '00':
            try:
                wy_data_dir = data_dict.get("day_history_wangyi")
                stock_index = i
                df1 = loadData(wy_data_dir,stock_index).sort_values("stock_date")
                stock = DF_to_StockDataFrame(df1)
                df_stock = stock_kdj(stock)
                #df_kdj_macd['adj_close'] = df_kdj_macd["macd"] 
                df_class = dayHistoryFeature.makeHistoryFeature(df_stock,10,"macdh")
                df_kdj_macd = df_class.df_out
                macd_feature_name = df_class.new_history_days_colname
                stock_date = now_date
                jjj = np.round(df_kdj_macd['kdjj'][df_kdj_macd['date']==now_date].values[0],3)
                macd_line = df_kdj_macd[macd_feature_name][df_kdj_macd['date']==now_date]
                stock_index_list.append(stock_index)
                j_line.append(jjj)
                stock_date_list.append(stock_date)
            except:
                pass
    return stock_index_list,j_line,stock_date_list
if __name__ == "__main__":
    now_date,now_date_time = get_the_datetime()
    now_date = now_date.replace('_','-')
    #now_date = '2020-06-19'
    stock_index_list,j_line,stock_date_list = allKdj(now_date)
    df_kdj_out = pd.DataFrame([stock_date_list,stock_index_list,j_line]).T
    df_kdj_out.columns = ['stock_date','stock_index','kdjj']
    df_kdj_out.sort_values('kdjj').to_csv('wy_kdj.csv',index=0)



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






