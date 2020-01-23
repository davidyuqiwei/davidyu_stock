from load_model_data import *

data_dir = "/home/davidyu/stock/data/test/for_every_stock"
file_name = "stock_mv_avg.csv"
df1 = read_mv_avg_data_clean(data_dir,file_name)
history_days = 30

df1.groupby("stock_index").apply(make_history_price,history_days=history_days)


fea_col = feature_columns()
feature_matrix,feature_names = make_features(df1,fea_col)

df1 = make_history_price(df1,history_days)
#df1 = make_history_vol(df1,history_days)
df1 = df1.drop(columns=['volume'])


