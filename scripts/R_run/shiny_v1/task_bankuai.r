bankuai_data=function(input){
    data_file = "/home/davidyu/stock/data/shiny_data/data/dfcf_bankuai.csv"
    data1 = read.csv(data_file)
    if(input$bankuai_tab=="地域"){
	    data1 = filter(data1,data_type=="diyu")
    }else if(input$bankuai_tab=="板块"){
	    data1 = filter(data1,data_type=="bankuai")
    }else if(input$bankuai_tab=="行业"){
	    data1 = filter(data1,data_type=="hangye")
    }
    data1$change_ratio=as.numeric(as.character(data1$change_ratio))
    return(data1)
}

bankuai_table_data=function(df1,input){
    date1 = as.character(input$date[1])
    #print(date1)
    df2 = filter(df1,dt==date1)
    df2 = select(df2,dt,bankuai_name,change_ratio,top_stock_name) 
    return(df2)
}
