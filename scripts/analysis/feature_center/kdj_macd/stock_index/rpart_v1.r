library(dplyr)
library(rpart)
library(rpart.plot)
#df1 = read.csv("/home/davidyu/stock/data/history_data/baostock/2020-12-17/601398.csv")
#df1 = read.csv("/home/davidyu/stock/scripts/davidyu_stock/scripts/analysis/feature_center/combine_data/stock_index/macd_v1.csv")
df1 = read.csv("/home/davidyu/stock/data/test/601318_macd_slope.csv")
df <- as.data.frame(df1)

df1 = df
df1$slope_dir = df1$slopes
df1$slope_dir[df1$slope_dir>0]=1
df1$slope_dir[df1$slope_dir<=0]=0

m<-rpart(slope_dir~rsi_6+rsi_12+kdjj+kdjk+kdjj+macdh+macdh_5_35_5+cci+wr_6,data=df1,method='class',cp=0.0065)

rpart.plot(m)
