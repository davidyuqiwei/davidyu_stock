from davidyu_cfg import *
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist
from functions.get_datetime import *
from functions.run_combine_all_csv import *


#print(df1.shape)
def print_buy_sale(df1):
	df2 = df1.drop_duplicates()
	df2 = df2[df2["status"] == "买盘"]
	df3 = df2.groupby(["stock_index","stock_name"]).count().sort_values("status",ascending=False)
	#print(df2.shape)
	#print("买盘")
	#print(df3["trade_time"].head(20))
	#print(df3["trade_time"].tail(20))
	df2 = df1.drop_duplicates()
	df2 = df2[df2["status"] == "卖盘"]
	df3 = df2.groupby(["stock_index","stock_name"]).count().sort_values("status",ascending=False)
	#print(df2.shape)
	#print("卖盘")
	#print(df3["trade_time"].head(20))
	#print(df3["trade_time"].tail(20))



def DADAN_diff_stat(df_input):
    df2 = df_input.drop_duplicates()
    ##
    df3 = df2[df2["status"] == "买盘"]
    #df3 = df2.groupby(["stock_index","stock_name"]).count().sort_values("status",ascending=False)
    df4 = df2.groupby(["stock_index","stock_name"])["trade_shou"].sum().reset_index()
    df4.columns = ["stock_index","stock_name","buy_num"]
    df5 = df2[df2["status"] == "卖盘"]
    df6 = df5.groupby(["stock_index","stock_name"])["trade_shou"].sum().reset_index()
    df6.columns = ["stock_index","stock_name","sale_num"]
    ## 
    df_merge = pd.merge(df4,df6,how='left',on = ["stock_index","stock_name"])
    df_merge["buy_sale_diff"] = df_merge["buy_num"]-df_merge["sale_num"]
    df_merge1 = df_merge.sort_values("buy_sale_diff",ascending=False)
    #print(df_merge1)
    return df_merge1
if __name__=='__main__':
	now_date,now_date_time = get_the_datetime()  ## the now_date is like "2019_11_08"
	#print(now_date)
	#now_date = "2019_11_08"
	dir_dadan = data_dict.get("DADAN")
	data_dir = os.path.join(dir_dadan,now_date)
	print(data_dir)
	df1 = combine_csv_in_folder(data_dir)
	df1.columns = ["stock_index","stock_name","trade_time",
	"price","trade_num","trade_shou","status",
	"price_change_rate","price_change_ratio","look"]
	
	
	print_buy_sale(df1)
	df_merge1 = DADAN_diff_stat(df1)
	print(df_merge1.head(30))
	#df_merge1[df_merge1['sale_num']=='NaN']
	
	df_merge2 = df_merge1[df_merge1.sale_num.isna()]   
	df_merge3 = df_merge2.sort_values("buy_num",ascending=False)  
	print(df_merge3.head(30))
	#df_merge1.to_csv("test.csv",encoding="utf_8_sig")



