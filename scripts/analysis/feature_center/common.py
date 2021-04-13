import pandas as pd
from davidyu_cfg import *
from functions.common.Regressions import *
from functions.common.dfcf_fuquan_data import *

# load historical data
df = dfcf_stock_data(stock_index)
