library("plotly")
library(dplyr)
trend_plot=function(input){
    tryCatch({
        stock_index = input$tr_stock_index
        start_date = input$tr_start_date
        end_date = input$tr_end_date
        data_file = paste0("/home/davidyu/stock/data/history_data/dfcf_fuquan/stock_index/",stock_index,"_fuquan.csv")
        data1 = read.csv(data_file)
        data1$dt = as.character(data1$dt)
        #print(end_date)
        data2=filter(data1,dt>=start_date,dt<=end_date)
        #print(data2)
        # 股东户数
        gd_file = paste0("/home/davidyu/stock/data/dfcf_gudonghushu/parse_data/",stock_index,".csv")
        df_g = read.csv(gd_file)
        df_g$stock_index = as.character(formatC(df_g$stock_index,width=6,flag='0'))
        df_g$dt = as.character(df_g$EndDate)
        stock_index1=stock_index
        df_g2 = filter(df_g,stock_index==stock_index1)
        #print(list(stock_index1=stock_index,start_date=start_date,df=df_g2))
    },error = function(e){
        print("error stock index input")
    },finally={
        print("finally")
    })
    p = plot_ly(data=data2,x=data2$dt,y=data2$close,type="scatter",mode="markers+lines",name="close")
    #p1 = plot_ly(data=data2,x=data2$dt,y=data2$open,type="scatter",mode="markers+lines")
    #p = add_trace(p,p1)
    #p %>% add_trace(data=data2,x=data2$dt,y=data2$open)
    p_out = p %>% add_trace(y=~data2$open,name="open") 
    p2 = plot_ly(data=data2,x=data2$dt,y=data2$turnover_rate,type="scatter",mode="markers+lines",name="换手率")
    p_gudong_num = plot_ly(data=df_g2,x=df_g2$EndDate,y=df_g2$HolderNum,type="scatter",mode="markers+lines",name="股东户数") %>% layout(xaxis=list(tickangle = 90,tickvals=df_g2$EndDate))
    return(list(p_out=p_out,p2=p2,p_gudong_num=p_gudong_num))
}    
