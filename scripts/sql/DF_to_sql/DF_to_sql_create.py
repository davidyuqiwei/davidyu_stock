import pandas as pd
import numpy

def get_df_column_type(df1):
    test_df_type = df1.iloc[0]
    types1 = [type(x) for x in test_df_type]
    types = []
    for i in types1:
        if i == numpy.int64:
            types.append('int')
        elif i == str:
            types.append('string')
        elif i == numpy.float64:
            types.append('decimal(38,2)')
    return types

def create_table(database_name,table_name,column_str,table_comment):
    a1 = """
use %s;
drop table if exists %s;

create table  if not exists %s(
%s
)
comment '%s' 
PARTITIONED BY ( day string comment '日期' )
row format delimited
fields terminated by '\\001'
stored as textfile;
    """ %(database_name,table_name,table_name,column_str,table_comment)
    print(a1)

def make_column_str(columns,types,comment):
    column_str = ''
    for i in range(0,len(columns)):
        str_list = [columns[i],types[i],'comment','\''+comment[i]+'\'']
        if i ==0:
            str_in = '\t'.join(str_list)+','
        elif i != len(columns)-1:
            str_in = '\t'.join(str_list)+','
            #column_str = column_str + str_in+'\n'+'\t'
        #print('\t'.join(str_list))
        else:
            str_in = '\t'.join(str_list)
        column_str = column_str + '\t'+str_in+'\n'
    return column_str
#print(column_str)

if __name__=='__main__':
    file_name = "/home/davidyu/stock/scripts/davidyu_stock/scripts/download/test/SH_50index.csv"
    df1 = pd.read_csv(file_name)
    columns = df1.columns.tolist()
    types = get_df_column_type(df1)
    #print(types)
    comment = columns
    database_name = "stock_test"
    table_name = "SH_50index"
    table_comment = 'SH_50index'
    column_str = make_column_str(columns,types,comment)
    #print(column_str)
    create_table(database_name,table_name,column_str,table_comment)

