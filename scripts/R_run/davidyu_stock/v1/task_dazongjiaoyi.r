dazongjiaoyi_data=function(input){
    dzjy = read.csv("/home/davidyu/stock/data/shiny_data/data/dazongjiaoyi.csv")
    dzjy$total_money = floor(dzjy$total_money)
    if(input$dazongjiaoyi_type=="正溢价"){
        data_out = filter(dzjy,data_type=="pos_zyl")   
        data_out1 = data_out[order(data_out$dt,data_out$total_money,decreasing=TRUE),]
        df2 = select(data_out1,stock_index,stock_name,dt,total_money,dazongjiaoyi_cnt,data_type) 
    }

    if(input$dazongjiaoyi_type=="全部"){
        data_out = filter(dzjy,data_type=="all")   
        data_out1 = data_out[order(data_out$dt,data_out$total_money,decreasing=TRUE),]
        df2 = select(data_out1,stock_index,stock_name,dt,total_money,dazongjiaoyi_cnt,data_type) 
    }

    if(input$dazongjiaoyi_type=="明细"){
        data_out = filter(dzjy,data_type=="detail")   
        data_out1 = data_out[order(data_out$dt,data_out$total_money,decreasing=TRUE),]
        df2 = select(data_out1,stock_index,stock_name,dt,total_money,buyername,salename)
    }
    return(df2)
}     
