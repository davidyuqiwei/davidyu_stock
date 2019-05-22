from package_path_define.path_define import *
from combine_all_csv1 import *

def add_stock_id(dir1):
    files=os.listdir(dir1)
    for fi in files:
        file1='\\'.join([dir1,fi])
        statinfo = os.stat(file1)
        size=statinfo.st_size
        if size>100:
            stk_id=fi.split('_')[0]
            #print(type(stk_id))
            df1=pd.read_csv(file1)
            df1['stockid']=stk_id.zfill(6)
            df1.to_csv('\\'.join([dir1,fi]),index=False,encoding="utf-8")
#add_stock_id(data_for_sql)

'''
df=pd.read_csv('\\'.join([dir1,fi]))
print(df.head())

'''
