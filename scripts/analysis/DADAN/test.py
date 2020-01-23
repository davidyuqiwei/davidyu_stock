from davidyu_cfg import *
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist
from functions.get_datetime import *
from functions.run_combine_all_csv import *

'''
update the date in df 
raw dataframe has not cover the download date,
which cannot choose by date
@ update time 2019-11-25
'''


#print(df1.shape)
def print_buy_sale(df1):
    df2 = df1.drop_duplicates()
    df2 = df2[df2["status"] == "买盘"]
    df3 = df2.groupby(["stock_index","stock_name"]).count().sort_values("status",ascending=False)
    df2 = df1.drop_duplicates()
    df2 = df2[df2["status"] == "卖盘"]
    df3 = df2.groupby(["stock_index","stock_name"]).count().sort_values("status",ascending=False)

def status_sum(df2,status):
    df3 = df2[df2["status"] == status]
    df4 = df3.groupby(["stock_index","stock_name"])["trade_num"].sum().reset_index()
    if status == "买盘":
        df4.columns = ["stock_index","stock_name","buy_num"]
    elif status == "卖盘":
        df4.columns = ["stock_index","stock_name","sale_num"]
    return df4
def DADAN_diff_stat(df_input):
    df2 = df_input.drop_duplicates()
    print("drop duplicate +++++++" )
    print(df2.shape)
    ##
    df4 = status_sum(df2,"买盘")
    df6 = status_sum(df2,"卖盘")
    ## 
    df_merge = pd.merge(df4,df6,how='left',on = ["stock_index","stock_name"])
    df_merge = df_merge.fillna(0)
    df_merge["buy_sale_diff"] = df_merge["buy_num"]-df_merge["sale_num"]
    df_merge1 = df_merge.sort_values("buy_sale_diff",ascending=False)
    #print(df_merge1)
    return df_merge1

if __name__ =='__main__':
    now_date,now_date_time = get_the_datetime()  ## the now_date is like "2019_11_08"
    #now_date = "2020_01_06"
    dir_dadan = data_dict.get("DADAN")
    data_dir = os.path.join(dir_dadan,now_date)
    print(data_dir)
    df1 = pd.read_csv("tt.csv")
    df1.columns = ["stock_index","stock_name", \
            "trade_time","price","trade_num","trade_shou","status","price_change_rate","price_change_ratio","look","date"]
    #df1[df1['stock_index']==600519].to_csv('mt.csv')
    #print_buy_sale(df1)
    df_merge1 = DADAN_diff_stat(df1)
    print(df_merge1.head(30))
    print(df_merge1.tail(30))
    #df_merge1.head(100).to_csv('tt.csv',index=0)
    #df_merge1[df_merge1['sale_num']=='NaN']
    
    df_merge2 = df_merge1[df_merge1.sale_num.isna()]   
    df_merge3 = df_merge2.sort_values("buy_num",ascending=False)  
    #print(df_merge3.head(30))
    #df_merge1.to_csv("test.csv",encoding="utf_8_sig")


