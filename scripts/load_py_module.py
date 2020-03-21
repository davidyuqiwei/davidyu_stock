from davidyu_cfg import *
from functions.connect_url import url_opener
from functions.ForDownload import generate_stock_index,stk_index_list_gen
from functions.data_dir import *
import time
from functions.make_dir import *
from functions.get_datetime import *  ## now_date,now_date_time = get_the_datetime()
from functions.LinearReg import LinearReg #
from functions.pyspark_functions import *

sc = spark.sparkContext
sc.setLogLevel("ERROR")

