library(rpart)
library(randomForest)

df1 = read.csv("/home/davidyu/stock/data/test/df_feature_import.csv")


df2=na.omit(df1)

m<-rpart(slopes~.,data=df2,method='class',cp=0.005)

a1 = df2[which(df2$rsi_6<47.375),]
a1 = df2[which(df2$rsi_6>=47.375),]

mean(a1$slope)

a2 = df2[which((df2$rsi_6<47.375)&(df2$cci<=-72.445)),]
a2 = df2[which((df2$rsi_6>=47.375)&(df2$cci>=86.08)),]

mean(a2$slope)
