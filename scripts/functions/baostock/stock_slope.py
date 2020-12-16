from davidyu_cfg import *
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist
from functions.get_datetime import *
from functions.run_combine_all_csv import *
from functions.colNames import *
from functions.day_history.kLines import klineDate
from functions.LinearReg import *

def stockSlope(stock_index,start_date,stat_days,pred_days):
    try:
	    data_dir = data_dict.get("baostock")
	    df1 = pd.read_csv(os.path.join(data_dir,"history_data",stock_index)+'.csv')
	    k1 = klineDate(start_date,stat_days,pred_days)
	    stat_end_date,pred_start_date,pred_end_date = k1.make_date()
	    df2 = df1[(df1["date"]>=pred_start_date)&(df1["date"]<=pred_end_date)]
	    slope = LinearReg.single_linear_reg(df2,"close")[0]
	    #print("{},{},{},{},{}".format(stock_index,pred_start_date,pred_end_date,pred_days,slope))
    except:
        #print("{},{},{},{},{}".format(stock_index,"aa","bb",pred_days,-999))
        slope = -999
        pred_start_date = -999
        pred_end_date = -999
    return slope,pred_start_date,pred_end_date
if __name__ =='__main__':
    stock_index = '601398'
    start_date = '2020-12-30'
    pred_days = 30
    stat_days = 1
    stockSlope(stock_index,start_date,stat_days,pred_days)
