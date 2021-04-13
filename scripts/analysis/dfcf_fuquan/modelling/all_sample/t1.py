import os
from input_para import *
from davidyu_cfg import *
from functions.common.TimeMake import timeFunc

now_date = timeFunc.getTheDatetime().get("now_date")
train_end_date = timeFunc.daysAgo(now_date,14)

data_dir = "/home/davidyu/stock/data/feature_center/combine_data"
files = os.listdir(data_dir)

files1 = [x for x in files if 'slope5' in x]
data_list = []
for i in files1:
    df1 = pd.read_csv(os.path.join(data_dir,i))
    df2 = df1[(df1["dt"]>='2019-01-01')]
    data_list.append(df2)
df3 = pd.concat(data_list) 
df3.to_csv("/home/davidyu/stock/data/test/xgb_test_data.csv",index=0)
