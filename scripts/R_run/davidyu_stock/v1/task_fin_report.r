library("plotly")
library(dplyr)
fin_report_plot = function(input){
	#data1 = read.csv("/home/davidyu/stock/data/shiny_data/data/fin_report.csv")
	load("/home/davidyu/stock/data/shiny_data/data/fin_report.RData")
	data2 = filter(data1,stock_index== input$fin_report_stock_index)
    indices_of_NAs <- which(data2 == -9999) 
    data2[which(data2==-9999,arr.ind = T)]="NULL"
    #replace(data2, indices_of_NAs, "NULL")
	data2 = data2[order(data2$dt),]
    col_select = input$fin_report_para
    source("col_names.r")
    col_index = which(name_fin_report==col_select)
    input_col = switch(col_index, "dt","meigushouyi","meiguweifenpeilirun","zhuyingyewulirunlv","maolirun","jinzichanshouyilv",
                       "guxifafanglv","zhuyingyewulirun","jinglirunzengzhanglv","zichanfuzhailv","stock_index")
    y_in = as.numeric(as.character(data2[,input_col]))
    y_in[y_in==-9999]=NA
    y_max= max(y_in)
    y_min= max(y_in)
	p = plot_ly(data=data2,x=data2$dt,y=y_in,type="scatter",mode="markers+lines") %>%layout(dtick=(as.numeric(y_max)-as.numeric(y_min))/5)
	return(p)   
}

