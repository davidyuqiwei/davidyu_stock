from functions.rolling_regression import *
file1 = "/home/davidyu/stock/data/tmp_data/day_history/fenhong_data.csv"
df1 = pd.read_csv(file1)

#rolling_regression(x,window,sort_col,reg_col)
slope_list = []
stock_index_list = []
for name,group in df1.groupby("stock_index"):
    df2 = group[group["stock_date"]>"2019-12-31"]
    t1 = LinearReg()
    slope, inter = t1.single_linear_reg(df2,"adj_close")
    slope_list.append(slope)
    stock_index_list.append(name)
    



