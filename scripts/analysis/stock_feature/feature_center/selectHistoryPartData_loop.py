from davidyu_cfg import *
import pandas as pd
from functions.DF_process import changeStockIndex
from functions.day_history.getDataFromSpark import *
from featureConfig import featureConfig
from functions.config import *

stk_list = featureConfig.rawDataStkList()


tmp_dir = featureConfig.raw_data_save_tmp_dir
n_part = featureConfig.raw_data_n_part
rawData_dir = featureConfig.rawData_dir
for i in range(0,n_part):
    logging.info("----------loop {}".format(str(i)))
    stk_diaoyan_tup = tuple(stk_list[i*20:i*20+20])
    save_name = featureConfig.raw_data_name%(str(i))
    save_file = os.path.join(rawData_dir,save_name)
    if not os.path.exists(save_file):
        para = {
            'stock_tuple': stk_diaoyan_tup,
            'start_date': '',
            'end_date': '',
            "save_file_name":save_name
            }
        getSparkData = getDataFromSpark(para)
        getSparkData.getDataFromSparkAll()
        tmp_file = os.path.join(tmp_dir,save_name)
        os.system("mv %s %s") %(tmp_file,rawData_dir)
    if os.path.exists(save_file):
        logging.info("-----file exists {}".format(save_file))
## move data to  /home/davidyu/stock/data/tmp_data/stock_feature/RollRegression
