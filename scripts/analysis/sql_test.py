
import pymysql
import  pymysql.cursors
import os

DB_NAME = 'stock'

# table_name=r'test2'
cnx= pymysql.connect(host='localhost',
	       database= DB_NAME,
	       user='root',
	       password='1988david',
	       #client_flags=[ClientFlag.LOCAL_FILES]
               charset='utf8'
	    )
cursor = cnx.cursor()
#print(ClientFlag.LOCAL_FILES)

query = "show tables"
cursor.execute(query)
for i in cursor:
    print(i)
