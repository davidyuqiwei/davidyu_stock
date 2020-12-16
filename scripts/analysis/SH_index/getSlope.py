from davidyu_cfg import *
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist
from functions.get_datetime import *
from functions.run_combine_all_csv import *
from functions.colNames import *
from functions.day_history.kLines import klineDate
from functions.LinearReg import *
from functions.common.cleanData import *


def getSlope(DF,start_date,stat_days,pred_days,col):
    df1 = cleanData.cleanColName(DF)
    df1 = cleanData.setDt(df1)
    df_columns = df1.columns
    if col not in df_columns:
        logging.error("no input slope columns: "+col)
        sys.exit(1)
    try:
        k1 = klineDate(start_date,stat_days,pred_days)
        stat_end_date,pred_start_date,pred_end_date = k1.make_date()
        df2 = df1[(df1["dt"]>=pred_start_date)&(df1["dt"]<=pred_end_date)]
        slope = LinearReg.single_linear_reg(df2,col)[0]
    except: 
        slope = -999
        pred_start_date = -999
        pred_end_date = -999
    return slope,pred_start_date,pred_end_date
if __name__ =='__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument("file_name",type=str,help="input file name")
    parser.add_argument("start_date",type=str,help="input start date")
    parser.add_argument("stat_days",type=int,help="input stat days")
    parser.add_argument("pred_days",type=int,help="input predict days")
    parser.add_argument("columns",default='close',type=str,help="input slope close columns")
    args = parser.parse_args()

    data_file = args.file_name
    start_date = args.start_date
    pred_days = args.pred_days
    stat_days = args.stat_days
    col = args.columns

    df1 = pd.read_csv(data_file)
    slope,pred_start_date,pred_end_date = getSlope(df1,start_date,stat_days,pred_days,col)
    #print(slope)
    print("{},{},{},{},{}".format('sh_index',pred_start_date,pred_end_date,pred_days,slope))

    # run example : python getSlope.py SH_'index_data.csv' '2020-10-30' 1 3 'close'
