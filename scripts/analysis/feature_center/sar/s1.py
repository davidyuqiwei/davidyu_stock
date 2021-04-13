import pandas as pd
from davidyu_cfg import *
from functions.common.Regressions import *
from functions.common.dfcf_fuquan_data import *
import talib
stock_index="601398"


df = dfcf_stock_data(stock_index)
sar = talib.SAR(df.high, df.low)

df["sar"] = sar

