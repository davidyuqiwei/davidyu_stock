from davidyu_cfg import *
from functions.LinearReg import LinearReg
from functions.rolling_regression import *
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import itertools
from functions.DF_process import changeStockIndex
from functions.config import *
class featureConfig:
    #### ----------- feature module setting ----------#
    ###################################################
    feature_dir = tmp_data_dict.get("stock_feature")
    #---------------- raw data setting ---------------#
    ###################################################
    ## how many parts of the raw data we will loop
    raw_data_n_part = 20
    # loop raw data name
    raw_data_name = "history_part%s.csv"
    # tmp save the raw data dir
    raw_data_save_tmp_dir = TMP_DATA_PATH['day_history_save_data_path']
    # finally save the raw data dir
    rawData_dir = os.path.join(feature_dir,"rawData")
    #---------------- rolling regression setting ----#
    rolling_regression_window = [5,20,30]
    def __init__(self):
        self.raw_data_name = "history_part%s.csv"
        self.feature_dir = tmp_data_dict.get("stock_feature")
    @staticmethod
    def makeFeatureSaveDir(featureName):
        feature_dir = tmp_data_dict.get("stock_feature")
        save_dir = os.path.join(feature_dir,featureName)
        create_dir_if_not_exist(save_dir)
        logging.info("--------- make the feature save dir {}".format(save_dir))
        return save_dir
    @staticmethod
    def rawDataInfo(i:int):
        '''
        with loop i =1
        make the rawData file name
        and raw Data dir_file_name
        '''
        raw_data_name = featureConfig.raw_data_name%(str(i))
        raw_file = os.path.join(featureConfig.feature_dir,"rawData",raw_data_name)
        return raw_data_name,raw_file
    @staticmethod
    def rawDataStkList():
        '''
        get the stock index list to loop to get
        part raw data
        '''
        data_dir = data_dict.get("basic_info")
        df1 = pd.read_csv(os.path.join(data_dir,"stock_basic_info.csv"))
        df1 = changeStockIndex(df1,'code')
        stk_diaoyan_list = df1['stock_index'].tolist()
        #stk_diaoyan_list.sort()
        stk_diaoyan_list = [x for x in stk_diaoyan_list if x[0:2] =='60' or x[0:2] =='00']
        return stk_diaoyan_list
