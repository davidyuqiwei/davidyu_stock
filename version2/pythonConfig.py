import sys
sys.path.append('/home/davidyu/stock/scripts/davidyu_stock/version2')
sys.path.append('/home/davidyu/stock/scripts/davidyu_stock/version2/sss')
from ttt.common.MakeDir import make_dir
#from scripts.functions.logModule.log_set import *
import os
# from functions.data_dir import *
#logging.info("load log module")
#logging.info("load data_dir module")
#logging.info("load make_dir module")


# the main data path
main_path = r"/home/davidyu/stock/"

data_path = os.path.join(main_path, "data")
# tmp path
tmp_data_path = os.path.join(main_path, "data", "tmp_data")

# script dir
script_path = os.path.join(main_path, "scripts/davidyu_stock/version2/scripts")
# download path
download_path = os.path.join(script_path, 'download')
# analysis
analysis_path = os.path.join(script_path, 'analysis')
# function
function_path = os.path.join(script_path, 'functions')
# all dirs
project_DIR = [data_path, download_path,tmp_data_path, analysis_path, function_path]


# add some path to the sys path to use the module
def print_add_sys_path():
    for dirs in project_DIR:
        sys.path.append(dirs)
        make_dir(dirs)



# add system path to python enviroment
print_add_sys_path()
# the python system path
# print("{:.^80}".format("python_path"))
