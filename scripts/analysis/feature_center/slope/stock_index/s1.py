from davidyu_cfg import *
from functions.data_dir import *
from functions.get_datetime import *
from functions.run_combine_all_csv import *
from functions.colNames import *
from functions.day_history.kLines import klineDate
from functions.LinearReg import *
from functions.common.slope.baoStockSlope import *


stock_index =  sys.argv[1]
start_date = sys.argv[2]
stat_days = sys.argv[3]
pred_days = sys.argv[4]
baoStockSlope(stock_index,start_date,int(stat_days),int(pred_days))




