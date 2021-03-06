from davidyu_cfg import *
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist
from functions.get_datetime import *
from functions.run_combine_all_csv import *
#from functions.pyspark_david.pyspark_functions import *
#from functions.pyspark_david.get_day_history_data import *


def load_data(date_in=None):
    dir_yjyq = data_dict.get("YeJiYuQi")
    now_date,now_date_time = get_the_datetime()
    if date_in == None:
        date_in = now_date
    data_dir = os.path.join(dir_yjyq,date_in)
    df1 = combine_csv_in_folder_raw(data_dir)
    df1.columns = ["index","stock_index","stock_name","yeji_predict","yeji_abstract","profit_change_ratio",
        "profit_change","date"]
    return df1

if __name__ == "__main__":
    df1 = load_data("2020_02_22")
    yeji_status = df1['yeji_predict'].unique().tolist()
    df2 = df1[(df1["yeji_predict"]=='业绩大幅上升')]
    print(df2.head())




'''
df2 = df1[(df1["yeji_predict"]=='业绩大幅上升')&(df1["date"]=="2020-01-04")]
stk_index_list = ['\''+str(x).zfill(6)+'\'' for x in df2.stock_index.tolist()]
stk_index_list = list(set(stk_index_list))
stk_index_list_str = ','.join(stk_index_list)
every_table = "stock_dev.day_history_insert"
start_date = "2020-01-04"
end_date = "2020-01-18"
df_history = get_data(every_table,start_date,end_date,stk_index_list_str)

#df_history.groupby('stock_index').apply(linear_REG)

data_vv = df_history.groupby('stock_index')
stock_ind = []
stock_slope = []
stock_row_len = []
for name,group in data_vv:
    slope,row_len = linear_REG(group)
    stock_ind.append(name)
    stock_slope.append(slope)
    stock_row_len.append(row_len)
    #print(slope)

data_dict = { 
        'stock_index': stock_ind,
        'slope': stock_slope,
        'row_len': stock_row_len
        }   
df_out = pd.DataFrame(data_dict)




def tt(x):
    #t1=x.high[0]
    print(x.head(3))
    #return t1





def filter_index(x):
    x1 = str(x).zfill(6)
    if x1[0:2] == '60' or x1[0:2] == '00':
        tag =1
    else:
        tag = 0
    return tag
df2 = df1[df1.stock_index.apply(filter_index)==1]


df2[df2.yeji_predict=="业绩大幅上升"]


'''
