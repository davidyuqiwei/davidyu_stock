setwd("/home/davidyu/stock/scripts/davidyu_stock/scripts/R_run")
library(dplyr)

df1 = read.csv("/home/davidyu/stock/data/history_data/baostock/2020-12-17/601398.csv")
df <- as.data.frame(df1)

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





