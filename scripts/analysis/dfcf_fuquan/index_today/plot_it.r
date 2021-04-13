library(dplyr)
df1 = read.csv("/home/davidyu/stock/scripts/davidyu_stock/scripts/analysis/dfcf_fuquan/index_today/macd_test.csv")

#plot(df1$rsi_6,df1$slopes)


df1$macdh_abs=abs(df1$macdh)
df1$slope1=df1$slopes
df1$slope1[df1$slopes>0]=1
df1$slope1[df1$slopes<=0]=0


df2 = filter(df1, dt>='2020-01-01')

#df2 = filter(df1, macdh_mvavg5<0,macdh>=0,kdjj<48.51)

df2 = filter(df1, macdh_mvavg5<0,macdh>=0)


filter(df1,kdjj>=109)
df3 = df2[order(df2$macdh_abs),]

plot(df3$rsi_6,df3$slopes)

#m<-rpart(slopes~rsi_6+rsi_12+rsi_24+kdjj+kdjk+kdjd+macdh+macdh_abs,data=df3,method='anova',cp=0.02)
#m<-rpart(slopes~rsi_6+rsi_12+rsi_24+kdjj+kdjk+kdjd+macdh+macdh_abs+macdh_mvavg3+macdh_mvavg5+macdh_mvavg10+macdh_abs+cci,data=df1,method='anova',cp=0.004)


m<-rpart(slope1~rsi_6+rsi_12+volume+wr_6+wr_10+rsi_24+kdjj+kdjk+kdjd+macdh+macdh_abs+macdh_mvavg3+macdh_mvavg5+macdh_mvavg10+macdh_abs+cci,data=df1,method='class',cp=0.003)

m<-rpart(slope1~rsi_6+rsi_12+wr_6+wr_10+rsi_24+kdjj+kdjk+kdjd+macdh+macdh_abs+macdh_mvavg3+macdh_mvavg5+macdh_mvavg10+macdh_abs+cci,data=df1,method='class',cp=0.002)

m<-rpart(slope1~rsi_6+rsi_12+wr_6+wr_10+rsi_24+kdjj+kdjk+kdjd+macdh+macdh_abs+macdh_mvavg3+macdh_mvavg5+macdh_mvavg10+macdh_abs+cci,data=df1,method='class',cp=0.001)





plot(m,ylim=c(0.98,1.2))
text(m,use.n=T,all=T,cex=0.7)



library(rpart.plot);
rpart.plot(m)

rpart.plot(m, branch=1, branch.type=2, type=1, extra=102,  
           shadow.col="gray", box.col="green",  
           border.col="blue", split.col="red",  
           split.cex=1.5, main="Kyphosis决策树");  

a1 = filter(df1,kdjj<109,rsi_6<35,rsi_12>45)


