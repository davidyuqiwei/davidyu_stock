import pandas as pd
from davidyu_cfg import *
from functions.LinearReg import LinearReg
from functions.rolling_regression import *
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import itertools
from functions.DF_process import changeStockIndex
from functions.pyspark_functions import *

featureName = "dazongjiaoyi"
feature_dir = tmp_data_dict.get("stock_feature")
save_dir = os.path.join(feature_dir,featureName)
create_dir_if_not_exist(save_dir)

for i in range(0,20):
    ## get raw split data
    raw_data_name = "history_part%s.csv"%(str(i))
    raw_file = os.path.join(feature_dir,"rawData",raw_data_name)
    df1 = pd.read_csv(raw_file)
    df1 = changeStockIndex(df1,'stock_index')
    ##
    stk_diaoyan_list = df1['stock_index'].tolist()
    #stk_diaoyan_list.sort()
    stk_diaoyan_list = [x for x in stk_diaoyan_list if x[0:2] =='60' or x[0:2] =='00']
    stk_list = tuple(set(stk_diaoyan_list))
    logging.info("----------loop {}".format(str(i)))

    sql1 = """
	select secucode as stock_index,stock_date,count(*) as dazongjiaoyi_cnt
	from stock_dev.dazongjiaoyi 
	where secucode in %s
	group by secucode,stock_date
	order by stock_date 
    """%(str(stk_list))

    my_dataframe = spark.sql(sql1)
    df2 = my_dataframe.toPandas()
    file_name = featureName+"_"+raw_data_name
    df2.to_csv(os.path.join(save_dir,file_name),index=0)

insert_colnames = ['dazongjiaoyi_cnt']
feature_name_list = np.load("feature_columns.npy")
update_feature_list = list(set(feature_name_list.tolist()+insert_colnames))
np.save("feature_columns.npy",update_feature_list)




