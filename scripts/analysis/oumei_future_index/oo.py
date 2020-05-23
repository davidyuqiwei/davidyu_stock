from davidyu_cfg import *
from functions.data_dir import *
import datetime


def str2date(x):
    try:
	    strs = x['date_str']
	    str_date = datetime.datetime.strptime(strs,"%Y-%m-%d")
	    day = str_date.weekday()+1
    except:
        day = -999
    return day



def process_date(df2):
	df2['date_str'] = df2['data_time'].str[0:10]
	df2 = df2[df2['date_str']!='data_time']
	df2['weekday'] = df2.apply(str2date,axis=1)
    return df2

data_dir = tmp_data_dict.get("oumei_future_index")

df1 = pd.read_csv(os.path.join(data_dir,"a.log"))
df2 = df1[df1['name']=='纳斯达克100']
df2 = process_date(df2)
save_file = os.path.join(data_dir,'nsdq.csv')
df2.sort_values('data_time').to_csv(save_file,index=0)

