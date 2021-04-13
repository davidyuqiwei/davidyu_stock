import_owner_data=function(input){
    import_owner = read.csv("/home/davidyu/stock/data/shiny_data/data/important_owner.csv")
    import_owner$num_change = as.numeric(as.character(import_owner$num_change))
    import_owner$liutong_ratio = as.numeric(as.character(import_owner$liutong_ratio))
    import_owner$stock_index = formatC(import_owner$stock_index,width=6,flag='0')
    data_out = import_owner[order(import_owner$report_date,decreasing=TRUE), input$show_vars, drop = FALSE]
    return(data_out)
}

