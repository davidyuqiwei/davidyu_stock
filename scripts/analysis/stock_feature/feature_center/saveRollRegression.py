import pandas as pd
from davidyu_cfg import *
from functions.rolling_regression import *
from functions.day_history.rollReg import rollRegDayHis
from featureConfig import featureConfig

## run to calculate the rolling regression
feature_dir = featureConfig.feature_dir
windows = featureConfig.rolling_regression_window
rolling_part_loop_len = featureConfig.raw_data_n_part
for i in range(0,5):
    for window in windows:
        raw_data_name = featureConfig.raw_data_name%(str(i))
        raw_file = os.path.join(featureConfig.rawData_dir,raw_data_name)
        save_file_name = "rollRegression_"+str(window)+'_'+raw_data_name
        save_file = os.path.join(feature_dir,"rollRegression",save_file_name)
        if not os.path.exists(save_file):
            df1 = pd.read_csv(raw_file)
            rollRegDayHis.getRollReg(raw_file,window,save_file)
        if os.path.exists(save_file):
            logging.info("file exists {}".format(save_file))
logging.info("finish rolling regression loop")
