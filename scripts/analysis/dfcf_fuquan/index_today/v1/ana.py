import pandas as pd
df5 = pd.read_csv("today_kdj_all.csv")
df6 = df5[df5["stock_date"]=="2021-02-22"]
df7 = df6[["stock_index","stock_date","rsi_6","macdh","macdh_mvavg5","macd","macds"]]
df7.sort_values("rsi_6").to_csv("rsi6_sort_today.csv",index=0)
df7["macdh_abs"] = df7["macdh"].abs()
df8 = df7[df7["macdh_mvavg5"]<0]
df8.round(3).sort_values("macdh_abs").to_csv("macdh_sort_today.csv",index=0)
df8.round(3).sort_values("macd").to_csv("macd_sort_today.csv",index=0)
