from davidyu_cfg import *
import pandas as pd
from functions.common.slope.baoStockSlope import *
from functions.feature_center.featureCenter import *


def featureSlope(date_col):
    out_slope = []
    df_out = pd.DataFrame()
    df_list = []
    for i in range(0,df1.shape[0]):
        for pred_days in pred_days_list:
            stock_index = str(df1["stock_index"][i]).zfill(6)
            start_date = df1[date_col][i]
            # get slope
            return_data = baoStockSlope(stock_index,start_date,stat_days,pred_days,if_print=0)
            slope = return_data.get("slope")
            pred_start_date = return_data.get("pred_start_date")
            pred_end_date = return_data.get("pred_end_date")
            out_slope.append(slope)

            df_list1 = df1.iloc[i,:].values.tolist() + [ slope,pred_start_date,pred_end_date,pred_days ]
            df_list.append(df_list1)
    df_out = pd.DataFrame(df_list)
    return df_out

if __name__ =='__main__':
    #data_dir = os.path.join(tmp_data_path,"feature_center")
    df1 = pd.read_csv("yx1.txt")
    #df1 = df1.head(5)
    df1.columns = ["stock_date","stock_index"]
    df1["stock_index"] = [x[3:9] for x in df1.stock_index.tolist()]                                                                                                         
    stat_days = 0
    #pred_days = 30
    pred_days_list = [5,10,15,20,30]
    date_col = 'stock_date'
    df_out = featureSlope(date_col)
    df_out.columns = df1.columns.tolist() + ["slope","pred_start_date","pred_end_date","pred_days"]
    df_out.to_csv("tt.csv",index=0)
