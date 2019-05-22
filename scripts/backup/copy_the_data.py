from package_path_define.path_define import *
from package_downloaddata.download_data_v1 import save_dir1

def copy_data_to_folder(folder1,sym,file_name,market=None,level=None):
    save_data_path1='\\'.join([main_path_data,folder1])
    print(sym)
    print(market)
    if not os.path.exists(save_data_path1):
        os.makedirs(save_data_path1)
    if market!=None:
        save_dir_fi='\\'.join([save_data_path1,sym,market])
    else:
        save_dir_fi='\\'.join([save_data_path1,sym])
    if level==1:
        file1='\\'.join([save_data_path1,file_name])
    print(file1)
    #print(file1)
    #if not os.path.isfile(file1):
    os.system(("cp %s %s") %(file_name,file1))
    #else:
    #   print("not")

#copy_data_to_foler(folder1,market,sym,file_name)
'''
csv1=os.listdir('./')
for fi in csv1:
    if fi.endswith(".csv"):
        print(fi)
#print(csv1)
#os.path.isfile(fname)
print(save_dir_fi)
'''
