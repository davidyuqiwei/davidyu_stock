import pandas as pd
df5 = pd.read_csv("./data/today_kdj_hs_300.csv")
df6 = df5[df5["dt"]==df5["dt"].max()]
df7 = df6[["stock_index","dt","macdh","macdh_mvavg5","macd","macds","rsi_6","rsi_12","kdjk","kdjd","kdjj"]]
df7["macdh_abs"] = df7["macdh"].abs()
df7 = df7[["stock_index","dt","macdh","macdh_abs","macdh_mvavg5","macd","macds","rsi_6","rsi_12","kdjk","kdjd","kdjj"]]
df7.to_csv("./data/kdj_macd_hs300.csv",index=0)




#df7["macdh_abs"] = df7["macdh"].abs()
#df8 = df7[df7["macdh_mvavg5"]<0]


#df8.round(3).sort_values("macdh_abs").to_csv("macdh_sort_today.csv",index=0)
#df8.round(3).sort_values("macd").to_csv("macd_sort_today.csv",index=0)
