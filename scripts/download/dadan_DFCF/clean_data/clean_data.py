from davidyu_cfg import *
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist
from functions.get_datetime import *
from functions.run_combine_all_csv import *
from functions.colNames import *
from functions.update.cleanData import cleanData
data_file = os.path.join(tmp_data_dict.get("dadan_DFCF"),"dadan_DFCF.csv")
df1 = pd.read_csv(data_file)

df1.columns = setColname().dadan_DFCF()
#df1 = df1[df1['zhuli_liuru_ratio']!="-"]
df1 = df1[df1['zhuli_liuru_ratio']!="zhuli_liuru_ratio"]
df1 = df1.replace("-",-9999)

df1 = cleanData.columnToFloat(df1,["new_price","today_increase_ratio","zhuli_liuru",
    'chaodadan_liuru', 'chaodadan_liuru_ratio','dadan_liuru', 'dadan_liuru_ratio', 'zhongdan_liuru',
    'zhongdan_liuru_ratio', 'xiaodan_liuru', 'xiaodan_liuru_ratio','zhuli_liuru_ratio'])

df1.drop_duplicates().to_csv(data_file,index=0)

