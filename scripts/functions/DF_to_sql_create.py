import pandas as pd
import numpy
df1 = pd.read_csv("/home/davidyu/stock/data/DADAN/2019_11_06/2019_11_06_105003.csv")

test_df_type = df1.iloc[0]

columns = ["stock_index","stock_name","trade_time",
        "price","trade_num","trade_shou","status",
        "price_change_rate","price_change_ratio","look"]

comment = columns
types1 = [type(x) for x in test_df_type]
types = []
for i in types1:
    if i == numpy.int64:
        types.append('int')
    elif i == str:
        types.append('str')
    elif i == numpy.float64:
        types.append('decimal(38,2)')

#columns = ["stock_index","stock_name","trade_time"]
#types = ['str','str','str','decimal(38,2)','int',
#        'int','str','decimal(38,2)','decimal(38,2)','str']

table_name = "DADAN"
table_comment = 'DADAN daily data'
def create_table(table_name,column_str,table_comment):
    a1 = """
    use stock_test;
    drop table if exists %s;
    
    create table  if not exists %s(
    %s
    )
    comment '%s' 
    PARTITIONED BY ( day string comment '日期' )
    row format delimited
    fields terminated by '\\001'
    stored as textfile;
    """ %(table_name,table_name,column_str,table_comment)
    print(a1)

#create_table(table_name)

column_str = ''
for i in range(0,len(columns)):
    str_list = [columns[i],types[i],'comment',comment[i]]
    if i ==0:
        str_in = '\t'.join(str_list)+','
    elif i != len(columns)-1:
        str_in = '\t'.join(str_list)+','
        #column_str = column_str + str_in+'\n'+'\t'
    #print('\t'.join(str_list))
    else:
        str_in = '\t'.join(str_list)
    column_str = column_str + '\t'+str_in+'\n'

#print(column_str)
create_table(table_name,column_str,table_comment)

