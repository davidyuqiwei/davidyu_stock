import pandas_datareader as web
start_date="2020-01-01"
end_date="2020-02-05"
df_dji = web.get_data_yahoo("^DJI",start_date,end_date)
df_sp500 = web.get_data_yahoo("^GSPC",start_date,end_date)


df1 = web.get_data_yahoo("%5EDJI",start_date,end_date)
df1 = web.get_data_yahoo("GC=F",start_date,end_date)








