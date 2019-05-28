import sys
import os 
main_path = "/home/davidyu/stock/"

## the main script path, and load the modules
script_path = os.path.join(main_path,"scripts/davidyu_stock/scripts") 
#print(script_path)

## the main data path
data_path = os.path.join(main_path,"data")


path_add=[script_path,data_path]
for dirs in path_add:
    sys.path.append(dirs)

import sys
## the python system path
print("{:.^80}".format(""))
print("{:.^80}".format("python_path"))
print("{:.^80}".format(""))
#print(sys.path)
[ print(x) for x in sys.path ]
print("{:.^80}".format(""))
print("{:.^80}".format(""))



'''
# the python all lib dirs
from distutils.sysconfig import get_python_lib
print(get_python_lib())

'''




