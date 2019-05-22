import pymysql.cursors
import pandas as pd
connect = pymysql.Connect(
    host='localhost',
    #port=3310,
    user='root',
    passwd='1988david',
    db='stock'
    #charset='utf8'
)

# 获取游标
cursor = connect.cursor()
#sql = "show tables"
#sql = "select * from fuquan limit 2"

##-------------
##======get the column names from database table
sql1="describe fuquan"
cursor.execute(sql1)
col=cursor.fetchall()
col_names=[]
for a1 in col:
    col_names.append(a1[0])
print(col_names)
##################################################

###======= get the data and transform to dataframe
sql = "select * from fuquan where stockid=600004"
#sql = "use stock"
cursor.execute(sql)
ret1 = cursor.fetchall()
#print([ret])
df1=pd.DataFrame(list(ret1),columns=col_names)
#df1.columns = cursor.keys()
print((df1.head()))
#print(type(ret1))
#print(connect.commit())



