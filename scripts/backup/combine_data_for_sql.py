from package_path_define.path_define import *
from combine_all_csv1 import *
from add_stock_id import *

### add id for stock data
#add_stock_id('g:\\stock\\data_to_sql_owner')
# combine all the csv in folder
combine_csv_in_folder('g:\\stock\\data_to_sql_owner')
'''
df=pd.read_csv('\\'.join([data_for_sql,fi]))
print(df.head())

'''
