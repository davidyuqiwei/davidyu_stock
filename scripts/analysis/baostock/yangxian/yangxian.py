from davidyu_cfg import *
from functions.data_dir import *
from functions.get_datetime import *
from functions.run_combine_all_csv import *
from functions.colNames import *
from functions.day_history.kLines import klineDate
from functions.LinearReg import *
from functions.common.dfProcess import *
from functions.common.loadModule.load_module_kdj import *
from scipy.stats import linregress




def stock_data(stock_index,start_date,end_date):
    df_dir = os.path.join(data_path,"history_data","baostock","2020-12-17")
    df1 = pd.read_csv(os.path.join(df_dir,stock_index+".csv"))
    df1 = df1[(df1["dt"]>=start_date)&(df1["dt"]<=end_date)]
    df1 = df1.drop_duplicates()
    df1 = df1.sort_values("date")
    df1["stock_index"] = [ x[3:9] for x in df1["code"]]
    return df1


def get_3_pos_line(df1):
    df1["line"] = df1["close"] - df1["open"]
    df1["line"][df1["line"]>0]=1
    df1["line"][df1["line"]<=0]=0
    df1['mv_close'] = df1.close.rolling(window=3).mean()
    df1['mv_close_120'] = df1.close.rolling(window=120).mean()
    df1['mv_close_250'] = df1.close.rolling(window=250).mean()
    df1['line_check_5'] = df1.line.rolling(window=5).sum()
    df1['line_check_3'] = df1.line.rolling(window=3).sum()
    df2 = df1[(df1["line_check_3"]==3)&(df1["close"]<df1['mv_close_250'])]
    return df2


if __name__ =='__main__':
    stock_index = sys.argv[1]
    start_date = '2017-01-01'
    end_date = '2020-12-17'
    try:
        df1 = stock_data(stock_index,start_date,end_date)
        df2 = get_3_pos_line(df1)
        #df3 = df2.tail(1)
        #print("{},{}".format(df2['date'].values,df2['code'].values))
        print(df2[["date","code"]].to_string(index=False,header=None))
    except:
        pass



