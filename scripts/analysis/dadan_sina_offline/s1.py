from davidyu_cfg import *
from functions.get_datetime import *  ## 

now_date,now_date_time = get_the_datetime()
#now_date = "2020_07_24"

#data_dir = data_
def get_dadan_sina_offline_data(now_date):
    data_dir = data_dict.get("dadan_sina_offline")
    #data_dir = "/home/davidyu/stock/data/dadan_sina/2020_07_06"
    file_name = [x for x in os.listdir(data_dir) if now_date in x][0]
    #file_name = "2020_07_08_154012.csv"
    df1 = pd.read_csv(os.path.join(data_dir,file_name))
    return df1

df1 = get_dadan_sina_offline_data(now_date)
df1['zhuli_buy_money'] = df1['avg_price'] *df1['zhuli_buy_vol']
df1['zhuli_buy_money_jing'] = df1['avg_price'] *df1['zhuli_buy_vol'] -df1['avg_price'] *df1['zhuli_sale_vol']

#df2 = df1.sort_values("zhuli_buy_money")
#df2[["stock_name","stock_index","zhuli_buy_money"]]

df3 = df1.sort_values("zhuli_buy_money_jing")
df_out = df3[["stock_name","stock_index","zhuli_buy_money","zhuli_buy_money_jing"]]

#df2 = df1.sort_values("zhuli_buy_money_jing",ascending=False)
#df3 = df2[["stock_name","stock_index","avg_price","zhuli_buy_vol","zhuli_buy_money","zhuli_buy_money_jing"]]
print(df_out.tail(50))




