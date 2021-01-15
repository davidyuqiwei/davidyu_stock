from davidyu_cfg import *
from functions.pyspark_functions import *
from functions.baostock.stock_return import *
from finquant.portfolio import build_portfolio

def port_val(pf):
    return_data = {'expected_return':pf.expected_return,
                   'volatility':pf.volatility,
                   'sharpe':pf.sharpe,
                   'skew':pf.skew,
                   'kurtosis':pf.kurtosis}
    return return_data


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
        limit 30
    """
    df1 = spark.sql(sql2)
    df2 = df1.toPandas()
    #stock_index_list = df1.select("stock_index_list").collect()
    return df2


df_jj = get_jijin_stock_group()
stock_index_list = df_jj.stock_index_list.values.tolist()
jj_name = df_jj.jijin_name.values.tolist()

out_data = []

for i,element in enumerate(stock_index_list): 
    try:
        a2 = element
        jj_name_in = jj_name[i]
        list1 = element
        list2 = "\""+list1.replace(",",",\"").replace(",\"","\",\"")+"\""
        sql3 = """
            select dt,lpad(stock_index_raw,6,'0') as stock_index,close
            from stock_dev.baostock_byyear
            where lpad(stock_index_raw,6,'0') in (%s)
        """%(list2)
        df_r1 = spark.sql(sql3)
        df_r2 = df_r1.toPandas()
        df_r2["close"] = [ np.float(x) for x in df_r2["close"].values.tolist()]
        df_r3 = pd.pivot_table(df_r2,index="dt",columns="stock_index",values="close")
        df_r4 = df_r3.dropna()
        df_r4.index.name = 'Date'
        #df_r4["portfolio_return"] = df_r4.sum(axis=1)
        df_r4.columns = df_r4.columns.values.tolist()
        pf = build_portfolio(data=df_r4)
        df_out = pd.DataFrame(port_val(pf))
        df_out["jijin_name"] = jj_name_in
        out_data.append(df_out)
    except:
        pass
df_f1 = pd.concat(out_data)
df_f1.to_csv("tt.csv",index=0)
#print(df_f1.reset_index())

