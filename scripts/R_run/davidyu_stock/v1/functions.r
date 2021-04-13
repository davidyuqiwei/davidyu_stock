col_to_float=function(data2,columns){
    for(i in columns){
       data2[,i] = as.numeric(as.character(data2[,i]))
    }
    return(data2)
}

