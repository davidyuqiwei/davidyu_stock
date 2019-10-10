## merge code

# -*- coding: utf-8 -*-
"""
Created on 2019-7-16 10:23
@author: HuangJiaxin
"""
import os

def file2txt():
    f=open(r"0930.txt","w",encoding='utf-8')
    for dirpath, dirnames, filenames in os.walk(r'D:\Users\YUQIWEI145\davidyu_document\doc\script_davidyu'):
        print('Directory', dirpath)
        for filename in filenames:
            print('File', filename)
            fp=os.path.join(dirpath,filename)
            f.write("\n$FilePath$\t{}\n".format(fp))
            with open(fp,'r',encoding='utf-8') as rf:
                f.writelines(rf.readlines())
    f.close()

def txt2file():
    dir=r'D:\Users\YUQIWEI145\davidyu_document\doc\script_davidyunew'
    with open(r"0930.txt","r",encoding='utf-8') as f:
        lines=f.readlines()
    idx_lst=[]
    fn_lst=[]
    for idx in range(len(lines)):
        if lines[idx][:10]=="$FilePath$":
            idx_lst.append(idx)
            fn=lines[idx].strip().split('\t')[-1]
            fn=fn.replace(r"D:\Users\YUQIWEI145\davidyu_document\doc\script_davidyu",dir)
            fn_lst.append(fn)
    idx_lst_r=idx_lst[1:]+[len(lines)]
    for i in range(len(fn_lst)):
        out_path = os.path.dirname(fn_lst[i])
        if not os.path.exists(out_path):
            os.makedirs(out_path)
        with open(fn_lst[i],'w',encoding='utf-8') as wf:
            wf.writelines(lines[(idx_lst[i]+1):(idx_lst_r[i]-1)])


if __name__ == "__main__":
    #file2txt()
    txt2file()