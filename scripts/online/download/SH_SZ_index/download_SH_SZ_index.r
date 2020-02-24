library(quantmod)

dateStart <- "1998-02-01"
dateEnd <- Sys.Date()

#dateEnd <-Sys.Date()
index=c("000001.sz","000001.ss")
file_name1=c("shenzhen_index_all.csv","shanghai_index_all.csv")

for (i in 1:2){
	result=getSymbols(index[i],from =dateStart,to = dateEnd,src = "yahoo",auto.assign=FALSE)
	time1=time(result)
	data1=data.frame(time=time1,result)	
	#file_name=paste0("shanghai_index_all.csv")
	file_name=file_name1[i]
	write.table(data1,file_name,row.names=FALSE,col.names=FALSE,sep=",")
}
#result=getSymbols("000001.ss",from =dateStart,to = dateEnd,src = "yahoo",auto.assign=FALSE)


#a1=getSymbols("DJI",from="2020-02-01",to="2020-02-03",src = "yahoo",auto.assign=FALSE)
#getSymbols("DJI", src = "yahoo", from ="2020-02-01", to="2020-02-05")

