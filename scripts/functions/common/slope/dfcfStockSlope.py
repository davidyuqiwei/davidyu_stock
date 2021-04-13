from davidyu_cfg import *
from functions.data_dir import *
from functions.get_datetime import *
from functions.run_combine_all_csv import *
from functions.colNames import *
from functions.day_history.kLines import klineDate
from functions.LinearReg import *

#stock_index = "600487"

def baoStockSlope(stock_index,start_date,stat_days,pred_days,if_print=1):
    stat_days = int(stat_days)
    pred_days = int(pred_days)
    df_dir = tmp_data_dict.get("baostock")
    df_dir = os.path.join(data_path,"history_data","dfcf_fuquan","stock_index")
    k1 = klineDate(start_date,stat_days,pred_days)
    stat_end_date,pred_start_date,pred_end_date = k1.make_date()
    try:
        df1 = pd.read_csv(os.path.join(df_dir,stock_index+".csv"))
        df1 = df1.drop_duplicates()
        df2 = df1[(df1["date"]>=pred_start_date)&(df1["date"]<=pred_end_date)]
        rows = df2.shape[0]
        slope = LinearReg.single_linear_reg(df2,"close")[0]
        if if_print ==1:
            print("{},{},{},{},{},{},{}".format(stock_index,start_date,pred_start_date,pred_end_date,pred_days,rows,slope))
    except:
        slope = -999
        rows = 0
        if if_print==1:
            print("{},{},{},{},{},{},{}".format(stock_index,start_date,pred_start_date,pred_end_date,pred_days,0,-999))
    return_data = dict(stock_index=stock_index, start_date=start_date, pred_start_date=pred_start_date,
            pred_end_date=pred_end_date,rows=rows,slope=slope) 
    return return_data
if __name__ =='__main__':
    stock_index = sys.argv[1]
    start_date = sys.argv[2]
    stat_days = sys.argv[3]
    pred_days = sys.argv[4]
    a1 = baoStockSlope(stock_index,start_date,stat_days,pred_days)
    print(a1.get("slope"))



