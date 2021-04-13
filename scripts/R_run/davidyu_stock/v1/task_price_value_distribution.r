library("plotly")
library(dplyr)
pv_data=function(input){
	stock_index = input$pv_stock_index
    #stock_index="601398"
    reset_date = input$reset_date
    if(reset_date=="0"){
        start_date = Sys.Date()-28
        end_date = Sys.Date()
        date_diff = as.numeric(end_date-start_date)
        #dates = as.character(seq(from=as.Date(start_date), by=1, length.out=30))
    }else{
        start_date = input$pv_start_date
        end_date = input$pv_end_date
        #print(end_date)
        date_diff = as.numeric(as.Date(end_date)-as.Date(start_date))
    }
    #start_date=Sys.Date()-28
	dates = as.character(seq(from=as.Date(start_date), by=1, length.out=date_diff))
    #print(dates)
    #y_col = input$y
	data_file = paste0("/home/davidyu/stock/data/shiny_data/data/vol_prirce_distr/pv_dist_",stock_index,".csv")
    data1 = read.csv(data_file)
    #print(head(data1))
    data1$dt = as.character(data1$dt)
    data1$price = as.numeric(as.character(data1$price))
    data1$vol = as.numeric(as.character(data1$vol))
    data2 = filter(data1,dt>=min(dates),dt<=max(dates))
    new_y_min = min(data2$price)-min(data2$price)*0.1
    new_y_max = max(data2$price)+max(data2$price)*0.1
    new_x_min = min(data2$vol)-min(data2$vol)*0.1
    new_x_max = max(data2$vol)+max(data2$vol)*0.7
    return(list(data=data1,dates=dates,new_y_min=new_y_min,new_y_max=new_y_max,
                new_x_min=new_x_min,new_x_max=new_x_max))
}
