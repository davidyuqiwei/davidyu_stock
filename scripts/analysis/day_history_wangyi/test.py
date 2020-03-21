from davidyu_cfg import *
import os
from functions.data_dir import *

save_dir = data_dict.get("tmp")
save_file = os.path.join(save_dir,"dazongjiaoyi_stock_list.csv")
os.system("sh /home/davidyu/stock/scripts/davidyu_stock/scripts/analysis/day_history_wangyi/run.sh %s"%(save_file))
