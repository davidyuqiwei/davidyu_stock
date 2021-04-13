import logging
from davidyu_cfg import *
def if_error_DF(df1,work_dir):
    import os
    import pandas as pd
    import logging
    try:
        if df1.shape[0] ==0:
            TNLog().error("error: {}".format(work_dir))
        else:
            TNLog().info("OK: {}".format(work_dir))
    except:
        TNLog().error("error: {}".format(work_dir))


