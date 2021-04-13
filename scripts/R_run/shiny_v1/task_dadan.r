library("plotly")
library(dplyr)
data_dadan=function(input){
    stock_index_in = input$stock_index_dadan
    start_date = input$start_date_dadan
    end_date = input$end_date_dadan
    #data_file = paste0("/home/davidyu/stock/data/test/dadan_",stock_index,".csv")
    data_file = "/home/davidyu/stock/data/shiny_data/data/dadan.RData"
    load(data_file)
    data2$dt = as.character(data2$dt)
    data2$stock_index = as.character(data2$stock_index)
    trans_columns = c("dadan_liuru","zhongdan_liuru","xiaodan_liuru","chaodadan_liuru","zhuli_liuru")
    source('functions.r')
    data1 = col_to_float(data2,trans_columns)
    data1 = filter(data1,dt>=start_date,dt<=end_date,stock_index==stock_index_in)
    data1 = data1[order(data1$dt),]
    return(data1)
}

plot_dadan=function(data1){
    unit_in=1000000
    p1 = plot_ly(data=data1,x=data1$dt,y=data1$chaodadan_liuru/unit_in,type="scatter",mode="markers+lines",name="超大单流入")%>% layout(yaxis=list(tickfont=list(size=10)),xaxis=list(tickfont=list(size=10)))
    p2 = plot_ly(data=data1,x=data1$dt,y=data1$dadan_liuru/unit_in,type="scatter",mode="markers+lines",name="大单流入") %>% layout(yaxis=list(tickfont=list(size=10)),xaxis=list(tickfont=list(size=10)))
    p3 = plot_ly(data=data1,x=data1$dt,y=data1$zhuli_liuru/unit_in,type="scatter",mode="markers+lines",name="主力流入") %>% layout(yaxis=list(tickfont=list(size=10)),xaxis=list(tickfont=list(size=10)))
    p4 = plot_ly(data=data1,x=data1$dt,y=data1$zhongdan_liuru/unit_in,type="scatter",mode="markers+lines",name="中单流入") %>% layout(yaxis=list(tickfont=list(size=10)),xaxis=list(tickfont=list(size=10)))
    p5 = plot_ly(data=data1,x=data1$dt,y=data1$xiaodan_liuru/unit_in,type="scatter",mode="markers+lines",name="小单流入")%>% layout(yaxis=list(tickfont=list(size=10)),xaxis=list(tickfont=list(size=10)))
    return(list(p1=p1,p2=p2,p3=p3,p4=p4,p5=p5))
}
