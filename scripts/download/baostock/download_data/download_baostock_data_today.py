from davidyu_cfg import *
from functions.data_dir import *
#from functions.get_datetime import *
from functions.common.TimeMake import *
from functions.run_combine_all_csv import *
from functions.colNames import *
import baostock as bs
# http://baostock.com/baostock/index.php/Python_API%E6%96%87%E6%A1%A3#.E5.8E.86.E5.8F.B2.E8.A1.8C.E6.83.85.E6.8C.87.E6.A0.87.E5.8F.82.E6.95.B0
def download_data(stock_index,start_date,end_date):
    data_dir = data_dict.get("baostock")
    lg = bs.login(user_id="anonymous", password="123456")
    try:
        if stock_index[0:2] == "60":
            stock_index_in = "sh."+stock_index
        else:
            stock_index_in = "sz."+stock_index
        df2 = bs.query_history_k_data_plus(stock_index_in,"date,code,open,high,low,close,volume,amount,turn,tradestatus,pctChg,peTTM,psTTM,pcfNcfTTM,pbMRQ,isST",start_date=start_date, end_date=end_date,frequency="d", adjustflag="1")
        save_file = os.path.join(data_dir,stock_index+".csv")
        df3 = df2.get_data()
        #print(df3)
        df3["open"] = [np.round(float(x),2) if x!='' else -999 for x in df3["open"].tolist()]
        df3["high"] = [np.round(float(x),2) if x!='' else -999 for x in df3["high"].tolist()]
        df3["close"] = [np.round(float(x),2) if x!='' else -999 for x in df3["close"].tolist()]
        df3["low"] = [np.round(float(x),2) if x!='' else -999 for x in df3["low"].tolist()]
        df3["amount"] = [int(float(x)) if x!='' else -999 for x in df3["amount"].tolist()]
        df3["turn"] = [np.round(float(x),3) if x!='' else -999 for x in df3["turn"].tolist()]
        df3["pctChg"] = [np.round(float(x),3) if x!='' else -999 for x in df3["pctChg"].tolist()]
        df3["peTTM"] = [np.round(float(x),3) if x!='' else -999 for x in df3["peTTM"].tolist()]
        df3["psTTM"] = [np.round(float(x),3) if x!='' else -999 for x in df3["psTTM"].tolist()]
        df3["pbMRQ"] = [np.round(float(x),3) if x!='' else -999 for x in df3["pbMRQ"].tolist()]
        df3["stock_index"] = [ x.split(".")[1] for x in df3["code"].values.tolist()]
        df3["dt"] = df3["date"]
        df3["volume"] = [int(x) if x!='' else -999 for x in df3["volume"].tolist()]
        #df3 = df3[["stock_index","dt","open","high","close","low","volume"]]
        df3.to_csv(save_file,index=0)
    except Exception as e:
        pass
        print("error")
        print(e)

if __name__ == "__main__":
    stock_index=str(sys.argv[1])
    #now_date,now_date_time = get_the_datetime()
    now_date,now_date_time = timeFunc.get_the_datetime()
    start_date = timeFunc.daysAgo(now_date,1)
    end_date = now_date
    #print(start_date)
    #start_date = now_date[0:8]+"01"
    download_data(stock_index,start_date,end_date)


'''
参数名称    参数描述
date    交易所行情日期
code    证券代码
open    开盘价
high    最高价
low 最低价
close   收盘价
preclose    昨日收盘价
volume  成交量（累计 单位：股）
amount  成交额（单位：人民币元）
adjustflag  复权状态(1：后复权， 2：前复权，3：不复权）
turn    换手率
tradestatus 交易状态(1：正常交易 0：停牌）
pctChg  涨跌幅
peTTM   动态市盈率
pbMRQ   市净率
psTTM   市销率
pcfNcfTTM   市现率
isST    是否ST股，1是，0否))

'''
