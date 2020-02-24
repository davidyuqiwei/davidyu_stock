from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist
import pandas as pd
import os
def combine_with_stock_basic_info(df_input,columns_select):
    out_columns = df_input.columns.tolist() 
    out_columns = out_columns + columns_select
    basic_info_dir = data_dict.get("basic_info")
    basic_info_df = pd.read_csv(os.path.join(basic_info_dir,"stock_basic_info.csv"))
    basic_info_df['stock_index'] = basic_info_df['code']
    basic_info_df['stock_index'] = [str(x).zfill(6) for x in basic_info_df['stock_index'].tolist()]
    df_input['stock_index'] = [str(x).zfill(6) for x in df_input['stock_index'].tolist()]
    df1 = pd.merge(df_input,basic_info_df,how='left',on = ["stock_index"])
    df2 = df1[out_columns]
    return df2
