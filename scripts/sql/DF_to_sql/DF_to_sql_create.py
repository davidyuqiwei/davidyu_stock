import pandas as pd
import numpy
from davidyu_cfg import *
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist

def get_df_column_type(df1):
    '''
    get the column type of DataFrame
    '''
    test_df_type = df1.iloc[0]
    types1 = [type(x) for x in test_df_type ]
    types = []
    for i in types1:
        if i == numpy.int64:
            types.append('int')
        elif i == str:
            types.append('string')
        elif i == numpy.float64:
            types.append('decimal(38,2)')
        elif i == float:
            types.append('decimal(38,2)')
        else:
            print(i)
    return types

def create_table_partition(database_name,table_name,column_str,table_comment):
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

def create_table(database_name,table_name,column_str,table_comment):
    a1 = """
use %s;
drop table if exists %s;

create table  if not exists %s(
%s
)
comment '%s' 
row format delimited
fields terminated by ','
stored as PARQUET;
    """ %(database_name,table_name,table_name,column_str,table_comment)
    print(a1)

def make_column_str(columns,types,comment):
    """
    @columns, a list of columns name
    @types column type
    @comment: the comment of column
    @return:  x1   string  COMMENT  '报告日期'
    """
    column_str = ''
    for i in range(0,len(columns)):
        str_list = [columns[i],types[i],'comment','\''+comment[i]+'\'']
        if i ==0:
            str_in = '\t'.join(str_list)+','
        elif i != len(columns)-1:
            str_in = '\t'.join(str_list)+','
        else:
            str_in = '\t'.join(str_list)
        column_str = column_str + '\t'+str_in+'\n'
    return column_str

if __name__=='__main__':
    '''
    sample_dir = tmp_data_dict.get("YeJiYuQi")
    #sample_dir = data_dict.get("baostock")
    filename = "YeJiYuQi.csv"
    file_name = os.path.join(sample_dir,filename)
    df1 = pd.read_csv(file_name,error_bad_lines=False)
    columns = df1.columns.tolist()
    types = get_df_column_type(df1)
    #print(types)
    '''
    columns = ["stock_index","start_date","end_date","pred_days","slope"]
    types = ["string","string","string","int","float"]
    comment = columns
    database_name = "stock_test"
    table_name = "stock_slope"
    table_comment = table_name
    column_str = make_column_str(columns,types,comment)
    #print(column_str)
    create_table(database_name,table_name,column_str,table_comment)

