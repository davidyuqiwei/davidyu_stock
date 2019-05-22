// :load /home/davidyu/stock/scripts/davidyu_stock/scripts/analysis/day_history/t1.scala
val sqlContext = new org.apache.spark.sql.hive.HiveContext(sc)

val date1="2018-09-12"
val date2="2018-12-20"
// which table to select
val table="stock_dev.day_history_insert"


val sql1 = s"""select 
	    min(struct(stock_date,adj_close,stock_index)).stock_index as stock_index,
	    min(struct(stock_date,adj_close,stock_index)).stock_date as min_date,
	    min(struct(stock_date,adj_close,stock_index)).adj_close as min_value,
	    max(struct(stock_date,adj_close,stock_index)).stock_date as max_date,
	    max(struct(stock_date,adj_close,stock_index)).adj_close as max_value,
	    round((max(struct(stock_date,adj_close,stock_index)).adj_close-min(struct(stock_date,adj_close,stock_index)).adj_close)/min(struct(stock_date,adj_close,stock_index)).adj_close,3) as diff_ratio,
        count(1) as days
	from $table
	where stock_date > '$date1' and stock_date < '$date2' 
	group by stock_index
    order by diff_ratio
"""

val df1 = sqlContext.sql(sql1)
//df1.show()

val sql2=""" select * from stock.stock_index """
val df2 =  sqlContext.sql(sql2)


df1.filter("days>30").join(df2,df1("stock_index") ===
df2("code")).select("stock_index","diff_ratio","name","industry",
"pb","holders","area").orderBy(desc("diff_ratio")).show(100)

case class Person(name : String,age : Int)

def test(p: Person){
    println(p.name)
    println(p.age)
}


val p1=Person("david",18)
test(p1)

/*
personDataFrame.join(orderDataFrame, personDataFrame("id_person") === 
orderDataFrame("id_person")).show()


val last_price=df1.orderBy(desc("stock_date")).limit(1).select("adj_close").collect().map(_(0))
val v1=last_price(0).toString.toDouble
val first_price=df1.orderBy("stock_date").limit(1).select("adj_close").collect().map(_(0))
val v2=first_price(0).toString.toDouble
val diff=v2-v1
val b =  diff.formatted("%.2f")
println(b)


    .collect()
val first_price=df1.orderBy("stock_date").limit(1)
    
    .collect()




*/
