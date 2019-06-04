import sys
import os 
main_path = "/home/davidyu/stock/"

## the main script path, and load the modules
script_path = os.path.join(main_path,"scripts/davidyu_stock/scripts") 
#print(script_path)

## the main data path
data_path = os.path.join(main_path,"data")
## donwload path
download_path = os.path.join(script_path,'download')
# analysis 
analysis_path = os.path.join(script_path,'analysis')

create_dir = ["test"]
project_DIR=[data_path,download_path,analysis_path]



#### add some path to the sys path to use the module
def print_sys_path():
    path_add=[script_path,data_path]
    for dirs in path_add:
        sys.path.append(dirs)
    ## the python system path
    print("{:.^80}".format(""))
    print("{:.^80}".format("python_path"))
    print("{:.^80}".format(""))
    #print(sys.path)
    [ print(x) for x in sys.path ]
    print("{:.^80}".format(""))
    print("{:.^80}".format(""))

print_sys_path()

#sys.path.append(script_path)
def make_project_dir(create_dir,project_DIR):
    '''
    update: 2019/05/29
    make a project some path,   download | anaysis | data
    if it is not exists
    '''
    for i in create_dir:
        for di in project_DIR:
            the_path = os.path.join(di,i)
            #print(the_path)
            isExists = os.path.exists(the_path)
            if not isExists:
                os.mkdir(the_path)
                print(the_path)
            else:
                pass
#make_project_dir(create_dir,project_DIR)

def rm_a_project(project_name,project_DIR):
    '''
    update: 2019/05/29
    remove a folder for in the path   ///   download | anaysis | data
    input yes/no to check it
    '''
    for di in project_DIR:
        the_path = os.path.join(di,project_name)
        a = print("make sure you want remove "+the_path)
        user_input = input("yes/no:")
        if user_input == 'yes':
            os.system("rm -rf %s" %the_path)
        else:
            print("recheck the code,we do not want remove the folder")
            sys.exit(1)
#rm_a_project("test",project_DIR)



'''
# the python all lib dirs
from distutils.sysconfig import get_python_lib
print(get_python_lib())

'''




