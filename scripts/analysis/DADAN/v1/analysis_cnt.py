from davidyu_cfg import *
#from functions.pyspark_functions import *
#from analysis_today_update import *
from functions.DF_process import changeStockIndex
from functions.basic_info.loadBasicInfo import loadBasicInfo
def stock_stat():
	df_mean = df1.groupby('stock_index')['buy_cnt'].sum() / trade_days
	df_mean = df_mean.reset_index().rename(columns={'buy_cnt':'buy_cnt_mean'})
	df_max = df1.groupby('stock_index')['buy_cnt'].max().reset_index().rename(columns={'buy_cnt':'buy_cnt_max'})

def buy_zerodays_per(x,trade_days):
    day_len = len(x[x['buy_cnt']>0])
    per = (trade_days - day_len)/trade_days 
    return np.round(per,3)
#df_zero_per = df1[df1['buy_cnt']>0].groupby('stock_index').apply(lambda x:buy_zerodays_per(x,trade_days))
save_dir = tmp_data_dict.get('DADAN')
df1 = pd.read_csv(os.path.join(save_dir,'DADAN_cnt_stat.csv'))
df1 = df1.drop_duplicates()
trade_days = df1['total_trade_date'][0]
df_zero_per = df1.groupby('stock_index').apply(lambda x:buy_zerodays_per(x,trade_days)).reset_index()
df_zero_per.columns = ['stock_index','zero_percent']
df_merge = pd.merge(df1,df_zero_per,"outer")
zero_prec_thres = 0.8
buy_cnt_thres = 20
df_select1 = df_merge[(df_merge['zero_percent']>zero_prec_thres)&(df_merge['buy_cnt']>buy_cnt_thres)]
df1 = loadBasicInfo().combine_with_stock_basic_info(df_select1)
out_col = df_select1.columns.tolist()+['name']
print(df1[out_col].sort_values('stock_date').head(50))
print(df1[out_col].sort_values('stock_date').tail(50))
#print(df_select1.sort_values('stock_date'))

'''
df_merge = pd.merge(df_max,df_zero_per,"outer")




df_t1 = pd.merge(df1,df_mean,"left")

df1['buy_cnt_var'] = (df_t1['buy_cnt'] - df_t1['buy_cnt_mean'])**2
df_std = df1.groupby('stock_index')['buy_cnt_var'].sum() / df1['total_trade_date'][0]
df_std = df_std.reset_index()

num_agg = {'buy_cnt':['max'], 'diff':['min', 'max']}
print(df1.groupby('stock_index').agg(num_agg))


df3 = df2.reset_index()

'''




