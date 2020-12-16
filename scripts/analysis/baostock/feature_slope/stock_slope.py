from davidyu_cfg import *
from functions.data_dir import *
from functions.get_datetime import *
from functions.run_combine_all_csv import *
from functions.colNames import *
from functions.day_history.kLines import klineDate
from functions.LinearReg import *
df_dir = data_dict.get("baostock")

#stock_index = "600487"



def stockSlope(stock_index,start_date,stat_days,pred_days):
    try:
        df1 = pd.read_csv(os.path.join(df_dir,stock_index+".csv"))
        k1 = klineDate(start_date,stat_days,pred_days)
        stat_end_date,pred_start_date,pred_end_date = k1.make_date()
        df2 = df1[(df1["date"]>=pred_start_date)&(df1["date"]<=pred_end_date)]
        
        slope = LinearReg.single_linear_reg(df2,"close")[0]
        print("{},{},{},{},{}".format(stock_index,pred_start_date,pred_end_date,pred_days,slope))
    except:
        print("{},{},{},{},{}".format(stock_index,"aa","bb",pred_days,-999))

if __name__ =='__main__':
    stock_index = sys.argv[1]
    start_date = sys.argv[2]
    stat_days = 1
    pred_days = int(sys.argv[3])
    stockSlope(stock_index,start_date,stat_days,pred_days)



