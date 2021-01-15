library(dplyr)
df1 = read.csv("/home/davidyu/stock/data/test/dfcf_fuquan_kdj.csv")
colnames(df1) = 

splitColName = function(x){
    strsplit(x,"\\.")[[1]][2]
}
new_name = sapply(colnames(df1),splitColName)
colnames(df1) = new_name
print(unique(df1$stock_index))
df3 = filter(df1, stock_index == '5')

df3$boll_ratio = df3$boll_ub/df3$boll_lb

plot(density(df3$boll_ratio))


df1$boll_ratio = df1$boll_ub/df1$boll_lb
df1 %>% 
    group_by(stock_index) %>%
    summarise(
        sum_value = quantile(boll_ratio,0.1)
    ) 


library(rpart)
df1 = read.csv("/home/davidyu/stock/data/test/kdj_reg_test.csv")

m<-rpart(slope_cls~rsi_6+rsi_12+rsi_24+kdjj+kdjk+kdjj+macdh+boll_ratio,data=df1,method='class',cp=0.01)

plot(m)
text(m,use.n=T,all=T,cex=0.9)

df1 = read.csv("/home/davidyu/stock/scripts/davidyu_stock/scripts/analysis/dfcf_fuquan/kdj/macd_continue.csv")

df2 = filter(df1, keys == 1)
df3 = filter(df1, keys == -1,stock_index==21)


