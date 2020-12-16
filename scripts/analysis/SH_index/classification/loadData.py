import pandas as pd
from davidyu_cfg import *
from functions.rolling_regression import *
from functions.day_history.rollReg import rollRegDayHis
from functions.logModule.log_set import *

data_file = "/home/davidyu/stock/data/SH_SZ_index/SH_index.csv"

df_stock = pd.read_csv(data_file)
df_stock.columns = [x.split(".")[1] for x in df_stock.columns]

logging.info("+++++++++++++++++++++++++++++++")
logging.info("load SH index data ")
logging.info(df_stock.head(10))



