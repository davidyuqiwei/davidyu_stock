library("plotly")
library(dplyr)
trend_plot=function(input){
    #stock_index=input$tr_stock_index
    #data_file = paste0("/home/davidyu/stock/data/history_data/dfcf_fuquan/stock_index/",stock_index,"_fuquan.csv")
    #data1 = read.csv(data_file)
    #
    tryCatch({
        stock_index1 = input$macd_stock_index
        start_date = input$macd_start_date
        end_date = input$macd_end_date
        
        data_file = paste0("/home/davidyu/stock/data/history_data/dfcf_fuquan/stock_index/",stock_index1,"_fuquan.csv")
        data1 = read.csv(data_file)
        data1$dt = as.character(data1$dt)
        #print(end_date)
        data_close=filter(data1,dt>=start_date,dt<=end_date)

        # macd1
        data_file = paste0("/home/davidyu/stock/data/shiny_data/data/macd/macd_",stock_index1,".csv")
        data1 = read.csv(data_file)
        data1$dt = as.character(data1$dt)
        data1$stock_index = as.character(formatC(data1$stock_index,width=6,flag='0'))
        data2=filter(data1,stock_index==stock_index1,dt>=start_date,dt<=end_date)
        print(head(data2))
        #print(data2)
        # 股东户数
       
        #print(list(stock_index1=stock_index,start_date=start_date,df=df_g2))
    },error = function(e){
        print("error stock index input")
    },finally={
        print("finally")
    })
ay <- list(
  tickfont = list(color = "red"),
  overlaying = "y",
  side = "right",
  title = "second y axis"
)
    p = plot_ly(data=data_close,x=data_close$dt,y=data_close$close,type="scatter",mode="markers+lines",name="close")
    #p = p %>% add_trace(y=~data2$macdh,name="macd_test",type="bar", yaxis = "y2") %>% layout(title = "Double Y Axis", yaxis2 = ay)
    #p_macd1 = plot_ly(data=data_close,x=data_close$dt,y=data_close$close,type="scatter",mode="markers+lines",name="close")
    #p=""
    p_macd1 = plot_ly(data=data2,x=data2$dt,y=data2$macdh,type="bar",name="macd_12_26_9")
    p_macd2 = plot_ly(data=data2,x=data2$dt,y=data2$macdh_5_34_5,type="bar",name="macdh_5_34_5")%>% add_lines(y=~data2$macd_5_34_5,name="macd__5_34_5",type="lines") %>% add_lines(y=~data2$macds_5_34_5,name="macds_5_34_5",type="lines")
    p_macd3 = plot_ly(data=data2,x=data2$dt,y=data2$macdh_13_55_8,type="bar",name="macdh_13_55_8")%>% add_lines(y=~data2$macd_13_55_8,name="macd_13_55_8",type="lines") %>% add_lines(y=~data2$macds_13_55_8,name="macds_13_55_8",type="lines")
    #p = plot_ly(data=data2,x=data2$dt,y=data2$macdh,type="scatter",mode="markers+lines",name="close")
    #p1 = plot_ly(data=data2,x=data2$dt,y=data2$open,type="scatter",mode="markers+lines")
    #p = add_trace(p,p1)
    #p %>% add_trace(data=data2,x=data2$dt,y=data2$open)
    #p_out = p %>% add_trace(y=~data2$open,name="open") 
    #p2 = plot_ly(data=data2,x=data2$dt,y=data2$turnover_rate,type="scatter",mode="markers+lines",name="换手率")
    #p_gudong_num = plot_ly(data=df_g2,x=df_g2$EndDate,y=df_g2$HolderNum,type="scatter",mode="markers+lines",name="股东户数") %>% layout(xaxis=list(tickangle = 90,tickvals=df_g2$EndDate))
    return(list(p_out=p,p2=p_macd1,p_macd2=p_macd2,p_macd3=p_macd3))
}    
