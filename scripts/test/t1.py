import pandas as pd
from davidyu_cfg import *
#del logging.basicConfig
from functions.common.errorLog import if_error_DF
"""
def if_error_DF(df1):
    import logging
    logging.basicConfig(level=logging.ERROR,filename="/home/davidyu/stock/log/error_log.log",
            filemode='a',
            format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')
    import os
    import pandas as pd
    try:
        if df1.shape[0] ==0:
            print("error")
            os.path.realpath(__file__)
    except:
        logging.error("error: {}".format(os.path.realpath(__file__)))

"""
dir_in = os.path.realpath(__file__)
df1 = pd.DataFrame({"a1":[1],"a2":[2]})
print(df1)
df2 = 4
if_error_DF(df2,dir_in)

