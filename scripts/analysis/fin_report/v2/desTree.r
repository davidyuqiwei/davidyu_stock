library(rpart)
library(randomForest)


df1 = read.csv("/home/davidyu/stock/data/tmp_data/financial_report/financial_report_ml_test_data.csv")

df1$change_rate[df1$change_rate>0]=1
df1$change_rate[df1$change_rate<=0]=-1

a1=df1[which((df1$x68_2016.12.31 < 13435350000)&(df1$x31_2016.12.31>=14.715)&(df1$x68_2016.12.31>=4853740000)&(df1$x9_2016.09.30>=0.4595)),]
a1=df1[which((df1$x68_2016.12.31 < 13435350000)&(df1$x31_2016.12.31>=14.715)&(df1$x68_2016.12.31<4853740000)&(df1$x9_2016.09.30>=0.4595)),]

table(a1$change_rate)


names(df1)
m<-rpart(change_rate~.,data=df1)


select x1,x94,x68,x21,x31
from stock_dev.fin_report 
where x68>=13435350000 and x21>=114.5 and x31>=20.9
and x1='2018-12-31'
order by x21 desc 
limit 30;



## xgboost
# https://xgboost.readthedocs.io/en/latest/build.html#r-package-installation


train_sub = sample(nrow(df1),7/10*nrow(df1))
train_data = df1[train_sub,]
test_data = df1[-train_sub,]

train_data$change_rate = as.factor(train_data$change_rate)
test_data$change_rate = as.factor(test_data$change_rate)
rf1 <- randomForest(change_rate ~ .,data=train_data,na.action = na.omit)
rf1 <- randomForest(change_rate ~ .,data=train_data,na.action = na.roughfix)


df_imp = as.data.frame(rf1$importance)
df_imp$label = rownames(df_imp)
df_imp[sort(df_imp$MeanDecreaseGini,index.return=TRUE)$ix,]　




