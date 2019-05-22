library(quantmod)

dateStart <- "1998-01-01"
<<<<<<< HEAD
dateEnd <- Sys.Date()

#dateEnd <-Sys.Date()
#result=getSymbols("000001.ss",from =dateStart,to = dateEnd,src = "yahoo",auto.assign=FALSE)
result=getSymbols("000001.sz",from =dateStart,to = dateEnd,src = "yahoo",auto.assign=FALSE)
time1=time(result)
data1=data.frame(time=time1,result)

#file_name=paste0("shanghai_index_all.csv")
file_name=paste0("shenzhen_index_all.csv")
=======
dateEnd <- "2018-03-21"

#dateEnd <-Sys.Date()
result=getSymbols("000001.ss",from =dateStart,to = dateEnd,src = "yahoo",auto.assign=FALSE)
time1=time(result)
data1=data.frame(time=time1,result)

file_name=paste0("shanghai_index_all.csv")
>>>>>>> 1f748b377819d67350ada8ca8130fda7752e2a91
write.table(data1,file_name,row.names=FALSE,col.names=FALSE,sep=",")




