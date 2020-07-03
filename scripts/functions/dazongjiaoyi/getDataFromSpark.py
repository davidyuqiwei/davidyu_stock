from davidyu_cfg import *
from functions.config import GET_DAY_HISTORY_DATA_PATH,TMP_DATA_PATH
from functions.data_dir import *
from functions.logModule.log_set import *
class getDataFromSpark():
    def __init__(self,para):
        self.test = 'test'
        self.save_file_name = para.get("save_file_name")
        self.cols = para.get('adj_close')
        self.stock_tuple = para.get('stock_tuple')
        self.start_date = para.get('start_date')
        self.end_date = para.get('end_date')
        if self.save_file_name is None:
            self.save_file_name = 'spark_select_data.csv'
            logging.info("----------None save_file_name set, set default to {}".format(self.save_file_name))
        if self.cols is None:
            self.cols = 'adj_close'
            logging.info("-----------None cols set, set default to {}".format(self.cols))
        self.save_dir = TMP_DATA_PATH['day_history_save_data_path']
    def getDataFromSpark(self):
        '''
        get the day history data from spark
        '''
        inputPara = " "+" ".join(["'%s'",'"%s"',"'%s'","'%s'","'%s'"])%(self.cols,str(self.stock_tuple),self.start_date,self.end_date,self.save_file_name)
        os.system("spark-submit "+os.path.join(GET_DAY_HISTORY_DATA_PATH,"save_data_to_csv.py")+ inputPara)
        logging.info("--------------- Finish Spark get data-----------")

    def getDataFromSparkAll(self):
        '''
        get the day history data from spark
        '''
        start_date = '1888-01-01'
        end_date = '2050-01-01'
        inputPara = " "+" ".join(["'%s'",'"%s"',"'%s'","'%s'","'%s'"])%(self.cols,str(self.stock_tuple),start_date,end_date,self.save_file_name)
        os.system("spark-submit "+os.path.join(GET_DAY_HISTORY_DATA_PATH,"save_data_to_csv.py")+ inputPara)
        logging.info("--------------- Finish Spark get data-----------")
    def loadDataFromSpark(self):
        df1 = pd.read_csv(os.path.join(self.save_dir,self.save_file_name))
        return df1
