import os
from dirs import *
class dir_control:
    def __init__(self,main_dir,dir_join_str):
        self.main_dir=main_dir
        self.dir_join_str=dir_join_str
    def data_dir(self,dir_in):
        """
        input value dir_in, a string[foler] like "david"
        or "david/david/david"
        """
        path_dict={}
        branch=set(dir_in)
        for i in branch:
            path=self.dir_join_str.join([self.main_dir,i])
            path_dict[i]=path
            isExists=os.path.exists(path)
            if not isExists:
                os.makedirs(path)
                print("create directory "+path)
        return path_dict
    def scripts_dir(self,script_dir_in):
        pass
dir_join_str="/"
## main dir
main_dir_data="/home/davidyu/data"
#main_dir_scripts="F:\davidyu\script\git\davidyu_stock\scripts"

p = dir_control(main_dir_data,dir_join_str)
path_dict=p.data_dir(data_dir)

"""
print(p.data_dir.__doc__)
print("\n\n")
print(p.data_dir.__dir__)
print(p.__dict__)
print("\n\n")
print(help(p.data_dir))
"""
#print(path_dict)
#data_dir=data_dir(main_dir,data_dir)



