from package_path_define.path_define import *
from package_downloaddata.download_data_v1 import save_dir1

def copy_data_to_foler(folder1,market,sym,file_name):
    save_data_path1='\\'.join([main_path_data,folder1,market,sym])
    print(save_data_path1)
    if not os.path.exists(save_data_path1):
        os.makedirs(save_data_path1)
    #save_dir_fi=save_dir1(save_data_path1,market,sym)
    #file1=os.path.join(save_dir_fi,file_name)
    #print(file1)
    os.system(("cp -rn %s %s") %(file_name,save_data_path1))

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
