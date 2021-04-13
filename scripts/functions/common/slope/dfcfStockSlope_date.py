from davidyu_cfg import *
from functions.data_dir import *
from functions.get_datetime import *
from functions.run_combine_all_csv import *
from functions.colNames import *
from functions.day_history.kLines import klineDate
from functions.LinearReg import *
from functions.common.dfcf_fuquan_data import *
#stock_index = "600487"

def dfcfStockSlope(stock_index,start_date="1900-01-01",end_date="2050-01-01",if_print=1):
    #df_dir = os.path.join(data_path,"history_data","dfcf_fuquan","stock_index")
    try:
        #data_file = os.path.join(df_dir,stock_index+"_fuquan.csv")
        #print(data_file)
        df1 = dfcf_stock_data(stock_index)
        df1 = df1.drop_duplicates()
        df2 = df1[(df1["dt"]>=start_date)&(df1["dt"]<=end_date)]
        rows = df2.shape[0]
        slope = LinearReg.single_linear_reg(df2,"close")[0]
        if if_print ==1:
            print("{},{},{},{},{}".format(stock_index,start_date,end_date,rows,slope))
    except:
        slope = -999
        rows = 0
        if if_print==1:
            print("{},{},{},{},{}".format(stock_index,start_date,end_date,0,-999))
    return_data = dict(stock_index=stock_index, start_date=start_date, end_date=end_date,
            rows=rows,slope=slope) 
    return return_data
if __name__ =='__main__':
    stock_index = sys.argv[1]
    start_date = sys.argv[2]
    end_date = sys.argv[3]
    a1 = dfcfStockSlope(stock_index,start_date,end_date)
    print(a1.get("slope"))



