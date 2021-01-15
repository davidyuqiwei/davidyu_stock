from davidyu_cfg import *
from functions.pyspark_functions import *
from functions.baostock.stock_return import *
from finquant.portfolio import build_portfolio


def get_jijin_stock_group():
    sql2 = """
        select jijin_name,
        concat_ws(',',collect_set(t2.code)) as stock_index_list
        from
        (
            select jijin_name,lpad(stock_index,6,'0') as stock_index
            from stock_dev.jijin 
            where stock_date = '2020-09-30' 
            and jijin_name like '%指数%'    
        ) t1
        left join
        stock.stock_index t2
        on t1.stock_index = lpad(t2.code,6,'0')
        group by jijin_name
        limit 5
    """
    df1 = spark.sql(sql2)
    stock_index_list = df1.select("stock_index_list").collect()
    return stock_index_list
stock_index_list = get_jijin_stock_group()

for s1 in stock_index_list: 
    a2 = s1
    list1 = a2.asDict().get('stock_index_list')
    list2 = "\""+list1.replace(",",",\"").replace(",\"","\",\"")+"\""
    sql3 = """
        select * from stock_dw.baostock_daily_return
        where stock_index in (%s)
    """%(list2)
    df_r1 = spark.sql(sql3)
    df_r2 = df_r1.toPandas()
    df_r3 = pd.pivot_table(df_r2,index="dt",columns="stock_index",values="daily_return")
    df_r4 = df_r3.dropna()
    df_r4.index.name = 'Date'
    print(df_r4.head(30))




