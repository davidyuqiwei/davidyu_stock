setwd("/home/davidyu/stock/scripts/davidyu_stock/scripts/R_run")
library(dplyr)
library(rpart)
library(rpart.plot)
#df1 = read.csv("/home/davidyu/stock/data/history_data/baostock/2020-12-17/601398.csv")
df1 = read.csv("/home/davidyu/stock/scripts/davidyu_stock/scripts/analysis/feature_center/combine_data/stock_index/macd_v1.csv")
df <- as.data.frame(df1)

df1 = df
df1$slope_dir = df1$slopes
df1$slope_dir[df1$slope_dir>0]=1
df1$slope_dir[df1$slope_dir<=0]=0
m<-rpart(slope_dir~rsi_6+rsi_12+kdjj+kdjk+kdjj+macdh+macdh_5_35_5+cci+wr_6,data=df1,method='class',cp=0.005)

rpart.plot(m)





df2 = filter(df, volume >0)
df2$date = as.Date(df2$date)
df3 = filter(df2, date > '2020-09-30')
plot(density(df3$close))

df3$close - lag(df3$close,1)
a1 = (df3$close - lag(df3$close,1))/df3$close
plot(density(a1[-1]))



require(PerformanceAnalytics); require(zoo)
data(edhec)
class(edhec) # [1] "xts" "zoo"
class(edhec$CTAGlobal) # "NULL"
var1<-rollapply(edhec,width=20,FUN=function(edhec) VaR(R=edhec,p=.95,method="modified"),by.column=TRUE)


aa = as.data.frame()
aa <- as.data.frame(a1[-1])
aa$date = df3$date[-1]
colnames(aa) = c("gs","date")

a2=xts(aa[,1], order.by=aa[,-1])





