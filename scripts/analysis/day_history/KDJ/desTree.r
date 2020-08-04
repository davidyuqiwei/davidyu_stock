library(rpart)
library(randomForest)


#df1 = read.csv("/home/davidyu/stock/data/test/day_history_kdj_macd_rsi_sample.csv")


df1 = read.csv("/home/davidyu/stock/data/test/SH_index_kdj_macd_rsi_test.csv")

m<-rpart(slopes~.,data=df1,method='class',cp=0.005)



df2 = df1[which(df1$kdjk<3.919),]
table(df2$slopes)

df2 = df1[which((df1$kdjk>=3.919)&(df1$rsi_6)>=99.38),]
table(df2$slopes)


rownames(m$frame)
m$splits

labels(m)



m$frame[yval2.V4]
m$frame$yval2.V4

m$frame$yval2[,4]
m$frame$yval2[,5]
m$frame$yval2[,6]


m<-randomForest(slopes~.,data=df1,ntrees=300)




